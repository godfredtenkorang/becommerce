from django.shortcuts import render, redirect
from .cart import Cart
from store.models import Product, Newsletter
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import ShippingFee
from decimal import Decimal

import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


# Create your views here.
def cart(request):
    cart = Cart(request)
    
    
    if request.method == 'POST':
        if 'apply_coupon' in request.POST:
            coupon_code = request.POST.get('coupon_code')
            if cart.apply_coupon(coupon_code):
                messages.success(request, f'Coupon "{coupon_code}" applied successfully!')
            else:
                messages.warning(request, f'Coupon "{coupon_code}" is not valid.')
            
        elif 'remove_coupon' in request.POST:
            cart.remove_coupon()
        return redirect('cart')
            
    context = {
        'cart': cart,
        'title': 'Cart',
        'shipping_fees': ShippingFee.objects.all(),
    }
    
    return render(request, 'cart/cart.html', context)

def add_cart(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, product_qty=product_quantity)
        
        cart_quantity = cart.__len__()
        
        reponse = JsonResponse({'qty' :cart_quantity})
        
        return reponse
    
def delete_cart(request):

    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)
        
        cart_quantity = cart.__len__()
        
        cart_total = cart.get_total()
        
        response = JsonResponse({'qty': cart_quantity, 'total':cart_total})
        
        return response
    
def update_cart(request):
    
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        
        cart.update(product=product_id, qty=product_quantity)
        
        cart_quantity = cart.__len__()
        
        cart_total = cart.get_total()
        
        response = JsonResponse({'qty': cart_quantity, 'total':cart_total})
        
        return response

