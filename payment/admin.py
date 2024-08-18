from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(ShippingAddress)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(Payment)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'address', 'phone_number', 'country', 'city', 'state', 'zipcode', 'user', 'amount', 'ref', 'verified', 'date_created']
    class Meta:
        model = Payment

admin.site.register(Payment, AdminPage)


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 3
  
  
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['full_name', 'email', 'shipping_address', 'amount_paid', 'user']}) ]
    inlines = [OrderItemInLine]
  
  
admin.site.register(Order, OrderAdmin)


class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'address', 'phone_number', 'country', 'city', 'state', 'zipcode', 'user']
    class Meta:
        model = ShippingAddress

admin.site.register(ShippingAddress, AdminPage)