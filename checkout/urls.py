from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('purchase_success/<distribution_number>', views.successful_payment, name='purchase_success'),

]