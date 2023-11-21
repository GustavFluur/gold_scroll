import uuid 
from django.db import models
from django.db.models import Sum
from django.conf import settings 

from articles.models import Article


# Create your models here.
class Customer_Order(models.Model):
    distribution_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    gender = models.CharField(max_length=80, null=True, blank=True)
    date_of_birth = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    sum_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def produce_distribution_number(self):
        
        return uuid.uuid4().hex.upper()
    
    def edit_total(self):

        self.order_total = self.lineitems.aggregate(Sum('lineItem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_SHIPPING:
            self.shipping_cost = self.order_total * settings.STANDARD_SHIPPING_PERCENTAGE / 100
        else:
            self.shipping_cost = 0
        self.grand_total = self.order_total + self.shipping_cost
        self.save()

    
    def save(self, *args, **kwargs):
        
        
        if not self.distribution_number:
             self.distribution_number = self.produce_distribution_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.distribution_number



class OrderLineItem(models.Model):
    order = models.ForeignKey(Customer_Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    article = models.ForeignKey(Article, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineItem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        self.lineitem_total = self.article.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'category {self.article.category} on order {self.order.distribution_number}'