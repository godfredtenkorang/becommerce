from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.utils import timezone

# Create your models here.

class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=300)
    email = models .EmailField(max_length=255)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20, default=0)
    country = models.CharField(max_length=20, default="Ghana")
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Shipping Address'
        
    def __str__(self):
        return 'Shipping Address - ' + str(self.id)


class Order(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    shipping_address = models.TextField(max_length=10000)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return "Order - #" + str(self.id)

CHOICES = (
    ('Processing', 'Processing'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=CHOICES, default="Not Delivered")
    
    def __str__(self):
        return "Order Item - #" + str(self.id)
