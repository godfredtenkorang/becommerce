from django.shortcuts import render, get_object_or_404, redirect
from .models import WishList, Review
from django.contrib.auth.decorators import login_required
from store.models import Product, Newsletter
from django.contrib import messages
from .forms import ReviewForm

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

@login_required()
def wishlist(request):
    wishlist_items = WishList.objects.filter(user=request.user)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    context = {
        'wishlist_items': wishlist_items,
        'title': 'Wishlist'
    }
    return render(request, 'wishlist/wishList.html', context)


def review_rate(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            reviews = Review.objects.get(user=request.user.id, product=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, "Thank you! Your review has been updated")
            else:
                messages.error(request, 'Please send your review again.')
                return render(request, 'store/product-info.html', {'form':form})
        
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Review()
                data.comment = form.cleaned_data['comment']
                data.rate = form.cleaned_data['rate']
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(
                    request, "Thank you! Your review has been submitted")
                
            else:
                messages.error(request, 'Please send your review again.')
                return render(request, 'store/product-info.html', {'form':form, 'product':product})
        return redirect(url)
    else:
        form = ReviewForm()
    return render(request, 'store/product-info.html', {'form': form, 'product':product})