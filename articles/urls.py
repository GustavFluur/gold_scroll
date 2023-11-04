from django.urls import path
from .import views

urlpatterns = [
    path('', views.omnis_articles, name='articles')
]

