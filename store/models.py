from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    date_added = models.DateTimeField('date added')
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['date_added',]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)
    
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
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'products'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    

PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class AppleSystem(models.Model):
    category = models.ForeignKey(Category, related_name='apple', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Apple systems'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('apple-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    
    
PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

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
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Laptops and Tablets'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('laptop-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    
    
PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class GamingLaptops(models.Model):
    category = models.ForeignKey(Category, related_name='gaming', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Gaming Laptops'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('gaming-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    
    
PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class ComputerAccessories(models.Model):
    category = models.ForeignKey(Category, related_name='accessory', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Computer Accessories'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('accessory-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    


PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class ComponentsAndParts(models.Model):
    category = models.ForeignKey(Category, related_name='component', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Components & Parts'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('component-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    

PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class SurveillanceSystems(models.Model):
    category = models.ForeignKey(Category, related_name='surveillance', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Surveillance Systems'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('surveillance-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    

PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class HeelsAndSlippers(models.Model):
    category = models.ForeignKey(Category, related_name='heels', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Heels and Slippers'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('heels-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    
    
PRODUCT_AVAILABILITY = (
    ('in stock', 'in stock'),
    ('out of stock', 'out of stock')
)

class ShoesAndSlippers(models.Model):
    category = models.ForeignKey(Category, related_name='shoe', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True)
    description1 = models.CharField(max_length=250, blank=True, default="")
    description2 = models.CharField(max_length=250, blank=True, default="")
    description3 = models.CharField(max_length=250, blank=True, default="")
    description4 = models.CharField(max_length=250, blank=True, default="")
    description5 = models.CharField(max_length=250, blank=True, default="")
    description6 = models.CharField(max_length=250, blank=True, default="")
    description7 = models.CharField(max_length=250, blank=True, default="")
    brand = models.CharField(max_length=100, default='un-branded')
    product_availability = models.CharField(max_length=20, choices=PRODUCT_AVAILABILITY, default='in stock')
    image1 = models.ImageField(upload_to='product1/img', default='default.jpg')
    image2 = models.ImageField(upload_to='product2/img', default='default.jpg')
    image3 = models.ImageField(upload_to='product3/img', default='default.jpg')
    normal_price = models.PositiveBigIntegerField(null=True)
    final_price = models.PositiveBigIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name_plural = 'Shoes and Slippers'
        ordering = ['date_added',]
        
    def get_absolute_url(self):
        return reverse('shoes-info', args=[self.slug])
        
    def __str__(self):
        return self.title
    
    
class Newsletter(models.Model):
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = 'Newsletters'
        
    def __str__(self):
        return self.email
    
    
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.name
    
    
class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner-img')
    
    class Meta:
        verbose_name_plural = 'Banners'
        
    def __str__(self):
        return self.name
