from django.shortcuts import render, HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("<h1>This is user</h1>")