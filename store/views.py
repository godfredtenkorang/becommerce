from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.db.models import Q # New

# Create your views here.
def index(request):
    laptopshops = LaptopsAndTablet.objects.all()
    
    context = {
        'laptopshops': laptopshops
    }
    return render(request, 'store/index.html', context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def productDetail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    context = {
        'product': product
    }
    return render(request, 'store/productDetail.html', context)

# def shopDetail(request, shop_slug):
#     shop = get_object_or_404(Shop, slug=shop_slug)
    
#     context = {
#         'shop': shop
#     }
#     return render(request, 'store/shopDetail.html', context)

def shop(request):
    shops = Product.objects.all()
    context = {
        'shops': shops,
    }
    return render(request, 'store/shop.html', context)

def search(request):
    search_item = request.GET.get('search')
    if search_item:
        search = Product.objects.filter(Q(title__icontains=search_item))
    else:
        search = Product.objects.all()
    context = {
        'search': search,
        'search_item': search_item
    }
    return render(request, 'store/search.html', context)



def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    
    products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
        'title': 'Categories'
    }
    return render(request, 'store/list-category.html', context)


# All Home Details

def laptopsandtablet(request, laptops_slug):
    laptop = get_object_or_404(LaptopsAndTablet, slug=laptops_slug)
    
    context = {
        'laptop': laptop
    }
    return render(request, 'store/laptopsDetail.html', context)