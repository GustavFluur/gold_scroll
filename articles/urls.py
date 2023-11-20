from django.urls import path
from .import views

urlpatterns = [
    path('', views.omnis_articles, name='articles'),
    path('<article_id>', views.article_detail, name='article_detail'),
    path('<int:pk>/remove/', views.remove_article, name='remove_article_detail'),
]

