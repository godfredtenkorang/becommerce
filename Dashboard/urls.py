# Dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adminDashbaord/', views.adminDashbaord, name='adminDashbaord'),
]
