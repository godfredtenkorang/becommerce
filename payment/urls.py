from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('make_payment/<str:ref>/',views.verify_payment, name='verify-payment'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-failed/', views.payment_failed, name='payment-failed'),
]

