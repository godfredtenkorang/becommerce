from django.contrib import admin
from .models import WishList, Review


# admin.site.register(WishList)

class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'added_on']
    class Meta:
        model = WishList

admin.site.register(WishList, AdminPage)


class AdminPage(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'comment', 'rate', 'created_at']
    class Meta:
        model = Review

admin.site.register(Review, AdminPage)