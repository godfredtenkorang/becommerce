from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    
    
    
    # Orders
    
    path('my-orders/', views.track_orders, name='myOrder'),
]