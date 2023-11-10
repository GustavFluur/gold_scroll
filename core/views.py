from django.shortcuts import render

from articles.models import Category, Article 

# Create your views here.
def index(request):
    articles = Article.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    print(articles)
    return render(request, 'core/index.html', {
        'categories': categories,
        'articles': articles,
    })