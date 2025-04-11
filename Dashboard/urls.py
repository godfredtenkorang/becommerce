# Dashboard/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', views.adminDashbaord, name='admin-dashboard'),
    path('orders/', views.orders, name='orders'),
    path('sales/', views.sales, name='sales'),
]
