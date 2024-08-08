from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>/', views.productDetail, name='product-info'),
    path('product/', views.shop, name='shop'),
    path('search/', views.search, name='search'),
    # path('product/<slug:shop_slug>/', views.shopDetail, name='shop-info'),
    
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    
    path('myOrder', views.myOrder, name='myOrder'),
    path('WishList', views.WishList, name='WishList'),
    
    
    # All Home Details
    
    path('product/<slug:laptops_slug>/', views.laptopsandtablet, name='laptop-info'),
]