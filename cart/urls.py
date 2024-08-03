from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/', views.add_cart, name='add-cart'),
    path('delete/', views.delete_cart, name='delete-cart'),
    path('update/', views.update_cart, name='update-cart'),
]

