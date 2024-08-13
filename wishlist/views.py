from django.shortcuts import render, get_object_or_404, redirect
from .models import WishList
from django.contrib.auth.decorators import login_required
from store.models import Product
from django.contrib import messages

@login_required(login_url='my-login')
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = WishList.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, "Your product has been added to wishlist")
        
    return redirect('WishList')

@login_required(login_url='my-login')
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    WishList.objects.filter(user=request.user, product=product).delete()
    
    return redirect('WishList')

@login_required(login_url='my-login')
def wishlist(request):
    wishlist_items = WishList.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items,
        'title': 'Wishlist'
    }
    return render(request, 'wishlist/wishList.html', context)

