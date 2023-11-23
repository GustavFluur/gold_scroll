from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from articles.models import Article


def acquisition_contents(request):

    acquisition_commodities = []
    total = 0
    article_count = 0
    acquisition = request.session.get('acquisition', {})

    for item_id, quantity in acquisition.items():
        article = get_object_or_404(Article, pk=item_id)
        total += (quantity * article.price)
        article_count += quantity
        acquisition_commodities.append({
            'item_id': item_id,
            'quantity': quantity,
            'article': article,
        })

 
    if total < settings.FREE_SHIPPING:
        delivery = total * float(Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100))
        free_shipping_distribution = settings.FREE_SHIPPING - total
    else:
        delivery = 0
        free_shipping_distribution = 0
    
    summary = delivery + total

    context = {
        'acquisition_commodities': acquisition_commodities,
        'total': total,
        'article_count': article_count,
        'delivery': delivery,
        'free_shipping_distribution': free_shipping_distribution,
        'FREE_SHIPPING': settings.FREE_SHIPPING,
        'summary': summary, 

    }

    return context