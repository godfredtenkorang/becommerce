from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Order, OrderItem, Payment, ShippingAddress
from cart.cart import Cart
from django.http import JsonResponse, HttpRequest
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import F


def checkout(request: HttpRequest) -> HttpResponse:
    
    cart = Cart(request)
    
    total_price = cart.get_all_total()

    user = request.user
    
    if request.user.is_authenticated:
        try:
            
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            
            if request.method == 'POST':
                full_name = request.POST['full_name']
                email = request.POST['email']
                address = request.POST['address']
                phone_number = request.POST['phone_number']
                country = request.POST['country']
                city = request.POST['city']
                state = request.POST['state']
                zipcode = request.POST['zipcode']
            
                payment = Payment(full_name=full_name, email=email, address=address, phone_number=phone_number, country=country, city=city, state=state, zipcode=zipcode, user=user, amount=total_price)
                payment.save()
                
                return render(request, 'payment/make_payment.html', {'cart': cart, 'title': 'Cart', 'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
            
            return render(request, 'payment/checkout.html', {'shipping': shipping_address, 'cart': cart, 'title': 'Cart'})

        except:
            if request.method == 'POST':
                full_name = request.POST['full_name']
                email = request.POST['email']
                address = request.POST['address']
                phone_number = request.POST['phone_number']
                country = request.POST['country']
                city = request.POST['city']
                state = request.POST['state']
                zipcode = request.POST['zipcode']
            
                payment = Payment(full_name=full_name, email=email, address=address, phone_number=phone_number, country=country, city=city, state=state, zipcode=zipcode, user=user, amount=total_price)
                payment.save()
                return render(request, 'payment/make_payment.html', {'cart': cart, 'title': 'Cart', 'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
            return render(request, 'payment/checkout.html')
    else:
        if request.method == 'POST':
            full_name = request.POST['full_name']
            email = request.POST['email']
            address = request.POST['address']
            phone_number = request.POST['phone_number']
            country = request.POST['country']
            city = request.POST['city']
            state = request.POST['state']
            zipcode = request.POST['zipcode']
        
            payment = Payment(full_name=full_name, email=email, address=address, phone_number=phone_number, country=country, city=city, state=state, zipcode=zipcode, amount=total_price)
            payment.save()
            
            return render(request, 'payment/make_payment.html', {'cart': cart, 'title': 'Cart', 'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
            
        context = {
            'title': 'Checkout',
            
        }

        return render(request, 'payment/checkout.html', context)
    
    
def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    
    if verified:
        payment.verified = True
        payment.save()
        
        for item in payment.items.all():
            product = item.product
            product.available_products = F('available_products') - item.quantity
            product.total_products = F('total_products') - item.quantity
            product.save()
        
        return redirect('payment-success')
    else:
        return redirect('payment-failed')

    
def complete_order(request):
    
    if request.POST.get('action') == 'post':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        
        # All-in-one shipping address
        
        shipping_address = "\n".join(filter(None, [address, phone_number, country, city, state, zipcode]))

        # Shopping cart informantion
        
        cart = Cart(request)
        
        # Get the total price of items
        
        total_cost = cart.get_all_total()
        
        '''
            Order variations
            
            1) Create order -> Account users WITH + WITHOUT shipping information
            
            2) Create order -> Guest users without an account
            
        '''
        # 1) Create order -> Account users WITH + WITHOUT shipping information
        
        if request.user.is_authenticated:
            order = Order.objects.create(full_name=full_name, email=email, shipping_address=shipping_address,
            amount_paid=total_cost, user=request.user
            )
            
            order_id = order.pk
            
            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], 
                                         price=item['final_price'], user=request.user)
        
        
        # 2) Create order -> Guest users without an account
        
        else:
            order = Order.objects.create(full_name=full_name, email=email, shipping_address=shipping_address,
            amount_paid=total_cost)
                    
            order_id = order.pk
                    
            product_list = []
            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['final_price'])
                product_list.append(item['product'])
                
            all_products = product_list
                
            # Email order
            
            send_mail('Order received', 'Hi! ' + '\n\n' + 'Thank you for picking your order' + '\n\n' +
                      'Please see your order below:' + '\n\n' + str(all_products) + '\n\n' + 'Total paid: $' + 
                      str(cart.get_all_total()), settings.EMAIL_HOST_USER, [email], fail_silently=False,)
            send_mail(
                f"New Order from {full_name}",
                f' end',
                    email,  # From email
                    [settings.EMAIL_HOST_USER],  # To email
                    fail_silently=False,
    ),
        order_success = True
        response = JsonResponse({'success':order_success})
        return response
    
def payment_success(request):
    
     # Clear shopping cart
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
            
    return render(request, 'payment/payment-success.html', {'title':'Payment success'})


def payment_failed(request):
    return render(request, 'payment/payment-failed.html', {'title':'Payment failed'})