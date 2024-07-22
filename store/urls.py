from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productDetail', views.productDetail, name='productDetail'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('category', views.category, name='category'),
    path('checkout', views.checkout, name='checkout'),
    path('myOrder', views.myOrder, name='myOrder'),
    path('WishList', views.WishList, name='WishList'),
]