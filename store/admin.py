from django.contrib import admin
from .models import *


# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(AppleSystem)
# admin.site.register(LaptopsAndTablet)
# admin.site.register(GamingLaptops)
# admin.site.register(ComputerAccessories)
# admin.site.register(ComponentsAndParts)
# admin.site.register(SurveillanceSystems)
# admin.site.register(HeelsAndSlippers)
# admin.site.register(ShoesAndSlippers)
# admin.site.register(Newsletter)
# admin.site.register(Contact)
# admin.site.register(Banner)

class ProductInLine(admin.TabularInline):
    model = Product
    extra = 1
    prepopulated_fields = {"slug": ("title",)}
  
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'slug']}), ('Date Information', {
        'fields': ['date_added'], 'classes': ['collapse']}), ]
    inlines = [ProductInLine]
    prepopulated_fields = {"slug": ("name",)}
  
  
admin.site.register(Category, CategoryAdmin)


class AdminPage(admin.ModelAdmin):
    list_display = ['id','name','email','phone','subject','message']
    class Meta:
        model = Contact

admin.site.register(Contact, AdminPage)


class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'email']
    class Meta:
        model = Newsletter

admin.site.register(Newsletter, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    class Meta:
        model = Banner

admin.site.register(Banner, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = AppleSystem

admin.site.register(AppleSystem, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = LaptopsAndTablet

admin.site.register(LaptopsAndTablet, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = GamingLaptops

admin.site.register(GamingLaptops, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = ComputerAccessories

admin.site.register(ComputerAccessories, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = ComponentsAndParts

admin.site.register(ComponentsAndParts, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = SurveillanceSystems

admin.site.register(SurveillanceSystems, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = HeelsAndSlippers

admin.site.register(HeelsAndSlippers, AdminPage)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7', 'brand', 'product_availability', 'image1', 'image2', 'image3', 'normal_price', 'final_price', 'date_added', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = ShoesAndSlippers

admin.site.register(ShoesAndSlippers, AdminPage)