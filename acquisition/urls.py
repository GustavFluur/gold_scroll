from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acquisition_view, name='acquisition_view'),
    path('add/<item_id>', views.add_to_acquisition, name='add_to_acquisition'),
]

