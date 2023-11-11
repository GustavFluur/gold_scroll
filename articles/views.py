from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def omnis_articles(request):

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, article_id):

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/articles_detail.html', context)