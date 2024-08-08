from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
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
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(default='un-branded')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    final_price = models.DecimalField(max_digits=4, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'products'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    
class Shop(models.Model):
    category = models.ForeignKey(Category, related_name='shop', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(default='un-branded')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    final_price = models.DecimalField(max_digits=4, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'shops'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('shop-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    
    

class LaptopsAndTablet(models.Model):
    category = models.ForeignKey(Category, related_name='laptop', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(default='un-branded')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    final_price = models.DecimalField(max_digits=4, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Laptops and Tablets'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('laptop-info', args=[self.slug])
        
    def __str__(self):
        return self.title