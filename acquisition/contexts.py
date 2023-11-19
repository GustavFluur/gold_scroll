from django.conf import settings

def acquisition_contents(request):

    purchase_items = []
    total = 0
    article_count = 0


    context = {
        'purchase_items': purchase_items,
        'total': total,
        'article_count': article_count,
    }

    return context