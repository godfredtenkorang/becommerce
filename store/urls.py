from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>/', views.productDetail, name='product-info'),
    path('product/', views.shop, name='shop'),
    path('search/', views.search, name='search'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('faQ/', views.faQ, name='faQ'),
    path('terms/', views.terms, name='terms'),
    # path('product/<slug:shop_slug>/', views.shopDetail, name='shop-info'),
    
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    
    
    # All Home Details
    
    path('product/<slug:laptops_slug>/', views.laptopsandtablet, name='laptop-info'),
    path('product/<slug:apple_slug>/', views.applesytem, name='apple-info'),
    path('product/<slug:gaming_slug>/', views.gaminglaptop, name='gaming-info'),
    path('product/<slug:accessory_slug>/', views.computer_accessories, name='accessory-info'),
    path('product/<slug:component_slug>/', views.component_and_parts, name='component-info'),
    path('product/<slug:surviellence_slug>/', views.surviellence_systems, name='surviellence-info'),
    path('product/<slug:heels_slug>/', views.heelsandslippers, name='heels-info'),
    path('product/<slug:shoe_slug>/', views.shoesandslippers, name='shoes-info'),
]