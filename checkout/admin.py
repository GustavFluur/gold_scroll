from django.contrib import admin
from .models import Customer_Order, OrderLineObject

# Register your models here.

class OrderLineObjectAdminInline(admin.TabularInline):
    model = OrderLineObject
    readonly_fields = ('lineObject_total',) 


class Customer_OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineObjectAdminInline,)

    readonly_fields = ('distribution_number', 'date',
                       'shipping_cost', 'order_total',
                       'sum_total','original_acquisition', 
                       'stripe_pid')

    fields = (  'distribution_number', 'first_name','last_name',
                'email', 'phone_number', 'country','zip_code', 
                'town_or_city', 'street_address1', 'street_address2', 
                'county', 'gender', 'date_of_birth', 'shipping_cost',
                'order_total', 'sum_total' 'original_acquisition', 
                       'stripe_pid',)
    
    list_display = ('distribution_number', 'first_name','last_name',
                    'order_total', 'shipping_cost',
                    'sum_total',)

        
    ordering = ('-date',)

admin.site.register(Customer_Order, Customer_OrderAdmin)

