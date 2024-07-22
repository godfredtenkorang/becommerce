from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/index.html')


def productDetail(request):
    return render(request, 'store/productDetail.html')

def shop(request):
    return render(request, 'store/shop.html')

def cart(request):
    return render(request, 'store/cart.html')

def category(request):
    return render(request, 'store/category.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def myOrder(request):
    return render(request, 'store/myOrder.html')


def WishList(request):
    return render(request, 'store/wishList.html')