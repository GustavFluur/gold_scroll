from django.shortcuts import render
from articles.models import Category, Article 
#from .forms import GoldSignUp

# Create your views here.
def index(request):
    articles = Article.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'articles': articles,
    })

#def register(request):
#    form = GoldSignUp()

#    return render(request, 'core/register.html',{
#        'form': form
#    })