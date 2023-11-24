from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    acquisition = request.session.get('acquisition', {})
    if not acquisition:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('articles'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NzOBUJzduBwqSE8C2wgQZiYAnGslRqdLY7Ab9z0ogX05NFsvY1nkXRwyIrNuLqgZqkBvGPWkHyHzooKDavt9HRy00IooGJpEL',
        'client_secret': 'sk_test_51NzOBUJzduBwqSE8dbWCtv7jIzi3VZH2Xopw6wx3B0x0pKBZCf4SPbwlKUb37B8G1Hp3U12y50YQAeMrNyaUiJwW004bq2VexU',
        
    }

    return render(request, template, context)