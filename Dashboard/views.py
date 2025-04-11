from django.shortcuts import render





def adminDashbaord(request):
    return render(request, 'Dashboard/adminDashbaord.html')

def orders(request):
    return render(request, 'Dashboard/orders.html')
