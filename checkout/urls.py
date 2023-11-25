from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('purchase_success/<distribution_number>', views.successful_payment, name='purchase_success'),
    path('cache_cart_payment_data/', views.cache_cart_payment_data, name='cache_cart_payment_data'),
    path('wh/', webhook, name='webhook'),

]

