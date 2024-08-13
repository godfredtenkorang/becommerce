from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>/', views.productDetail, name='product-info'),
    path('product/', views.shop, name='shop'),
    path('search/', views.search, name='search'),
    # path('product/<slug:shop_slug>/', views.shopDetail, name='shop-info'),
    
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    
    
    # All Home Details
    
    path('product/<slug:laptops_slug>/', views.laptopsandtablet, name='laptop-info'),
]