from django.shortcuts import render





def adminDashbaord(request):
    return render(request, 'Dashboard/adminDashbaord.html')

def orders(request):
    return render(request, 'Dashboard/orders.html')

def sales(request):
    return render(request, 'Dashboard/sales.html')
