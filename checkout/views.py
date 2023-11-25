from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Customer_Order, OrderLineObject
from articles.models import Article
from acquisition.contexts import acquisition_contents

import stripe
import json


@require_POST
def cache_cart_payment_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'acquisition': json.dumps(request.session.get('acquisition', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)



def checkout(request):
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        acquisition = request.session.get('acquisition', {})

        customer_order_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'zip_code': request.POST['zip_code'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'gender': request.POST['gender'],
            'date_of_birth': request.POST['date_of_birth'],
        }
        order_form = OrderForm(customer_order_data)
        if customer_order_data.is_valid():
            order = customer_order_data.save()
            for item_id, item_data in acquisition.items():
                try:
                    article = Article.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_object = OrderLineObject(
                            order=order,
                            article=article,
                            quantity=item_data,
                        )
                        order_line_object.save()
                except Article.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('acquisition_view'))

            request.session['save_purchase_data'] = 'save_purchase_data' in request.POST
            return redirect(reverse('purchase_success', args=[order.distribution_number]))
        else:
            messages.error(request, 'Your order form did not proceed accordingly due to an error! Please check it again! ')
    else:    
        acquisition = request.session.get('acquisition', {})
        if not acquisition:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('articles'))

        contemporary_acquisition = acquisition_contents(request)
        overall = contemporary_acquisition['summary']
        stripe_total = round(overall * 100)
        stripe.api_key = stripe_secret_key
        card_objective = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )


        order_form = OrderForm()


    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        #'client_secret': client_secret,
        
    }

    return render(request, template, context)


def successful_payment(request, distribution_number):

    save_purchase_data = request.session.get('save_purchase_data')
    order = get_object_or_404(Order, distribution_number=distribution_number)

    messages.success(request, f'Your order has been received! \
        Your shipping number is {distribution_number}. A confirmation \
        will be sent to {order.email}.')

    if 'acquisition' in request.session:
        del request.session['acquisition']

    template = 'checkout/purchase_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

