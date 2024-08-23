from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='WishList'),
    path('add/<int:product_slug>/', views.add_to_wishlist, name='add-to-wishlist'),
    path('remove/<int:product_slug>/', views.remove_from_wishlist, name='remove-from-wishlist'),
    
    # Review
    path('review/<int:product_id>/', views.review_rate, name='review'),
]