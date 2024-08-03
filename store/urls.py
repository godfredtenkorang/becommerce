from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>/', views.productDetail, name='product-info'),
    path('shop', views.shop, name='shop'),
    
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    path('checkout', views.checkout, name='checkout'),
    path('myOrder', views.myOrder, name='myOrder'),
    path('WishList', views.WishList, name='WishList'),
]