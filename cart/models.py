from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=100, unique=True)
    discount_percentage = models.IntegerField()
    
    def __str__(self):
        return f"{self.code} - {self.discount_percentage}"
    

class ShippingFee(models.Model):
    region = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.region