from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def productDetail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    context = {
        'product': product
    }
    return render(request, 'store/productDetail.html', context)

def shop(request):
    return render(request, 'store/shop.html')



def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    
    products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
        'title': 'Categories'
    }
    return render(request, 'store/list-category.html', context)

def checkout(request):
    return render(request, 'store/checkout.html')

def myOrder(request):
    return render(request, 'store/myOrder.html')


def WishList(request):
    return render(request, 'store/wishList.html')