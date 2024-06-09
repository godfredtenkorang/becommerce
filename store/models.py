from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['date_added',]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.CharField(default='un-branded')
    image = models.ImageField(upload_to='product/img', default='default.jpg')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'products'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
        
    def __str__(self):
        return self.title