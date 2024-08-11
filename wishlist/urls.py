from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='WishList'),
    path('add/<int:product_id>/', views.add_to_wishlist, name='add-to-wishlist'),
    path('remove/<int:product_id>/', views.remove_from_wishlist, name='remove-from-wishlist')
]