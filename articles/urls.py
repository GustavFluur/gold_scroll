from django.urls import path
from .import views

urlpatterns = [
    path('', views.omnis_articles, name='articles'),
    path('<article_id>', views.article_detail, name='article_detail'),
]

