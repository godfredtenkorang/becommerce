from django.shortcuts import render



def adminDashbaord(request):
    return render(request, 'Dashboard/adminDashbaord.html')
