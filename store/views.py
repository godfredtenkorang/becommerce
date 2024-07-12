from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/index.html')


def productDetail(request):
    return render(request, 'store/productDetail.html')

def shop(request):
    return render(request, 'store/shop.html')