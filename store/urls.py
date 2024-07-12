from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productDetail', views.productDetail, name='productDetail'),
    path('shop', views.shop, name='shop')
]