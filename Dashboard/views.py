from django.shortcuts import render
from payment.models import OrderItem




def adminDashbaord(request):
    return render(request, 'Dashboard/adminDashbaord.html')

def orders(request):
    orders = OrderItem.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'Dashboard/orders.html', context)

def sales(request):
    return render(request, 'Dashboard/sales.html')
