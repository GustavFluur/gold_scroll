from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Article

# Create your views here.


def omnis_articles(request):

    articles = Article.objects.all()
    query = None 

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "search criteria denied - please search again!")
                return redirect(reverse('articles'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            articles = articles.filter(queries)

    context = {
        'articles': articles,
        'search_keyword': query,
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, article_id):

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/articles_detail.html', context)