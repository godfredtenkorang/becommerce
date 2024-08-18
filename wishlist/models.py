from django.db import models
from store.models import Product
from django.contrib.auth.models import User


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Wishlists'
        unique_together = ('user', 'product')
        
    def __str__(self):
        return f"{self.user.username}'s wishlist"
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "reviews"
    
    def __str__(self):
        return self.product.title