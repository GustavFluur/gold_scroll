from django.shortcuts import render
from .models import Article

# Create your views here.


def omnis_articles(request):

    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)