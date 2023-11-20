from decimal import Decimal
from django.conf import settings


def acquisition_contents(request):

    acquisition_commodity = []
    total = 0
    article_count = 0

    if total < settings.FREE_SHIPPING:
        delivery = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_distribution = settings.FREE_SHIPPING - total
    else:
        delivery = 0
        free_shipping_distribution = 0
    
    summary = delivery + total

    context = {
        'acquisition_commodity': acquisition_commodity,
        'total': total,
        'article_count': article_count,
        'delivery': delivery,
        'free_shipping_distribution': free_shipping_distribution,
        'FREE_SHIPPING': settings.FREE_SHIPPING,
        'summary': summary, 



    }

    return context