from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.utils import timezone
from .paystack import PayStack
import secrets

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
    date_ordered = models.DateTimeField('date ordered', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f"Order - #{self.id} from {self.email}"

CHOICES = (
    ('Order Placed', 'Order Placed'),
    ('Waiting to be Shipped', 'Waiting to be Shipped'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
    
)
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=CHOICES, default="Order Placed")
    
    class Meta:
        verbose_name_plural = 'Order Items'
        ordering = ['-date_added']
    
    def __str__(self):
        return f"Order Item - #{self.id} - {self.order}"


class Payment(models.Model):
    full_name = models.CharField(max_length=300, default="")
    email = models .EmailField(max_length=255, default="")
    address = models.CharField(max_length=300, default="")
    phone_number = models.CharField(max_length=20, default=0)
    country = models.CharField(max_length=20, default="Ghana")
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveBigIntegerField(default=0)
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Payments'
        
    def __str__(self) -> str:
        return f"Payment: {self.amount}"
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
        
    def amount_value(self) -> int:
        return self.amount * 101
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 101 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False