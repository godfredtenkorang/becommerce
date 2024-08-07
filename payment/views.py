from django.shortcuts import render
from .models import ShippingAddress, Order, OrderItem
from cart.cart import Cart
from django.http import JsonResponse

# Create your views here.

def checkout(request):
    
    # User with account -- pre fill the form
    
    if request.user.is_authenticated:
        try:
            # Users with shipping information
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            
            context = {'shipping': shipping_address}
            
            return render(request, 'payment/checkout.html', context)
        
        except:
            # Users without shipping information
            
            return render(request, 'payment/checkout.html')
    
    else:
    # Guest User
    
        context = {
            'title': 'Checkout'
        }
    
        return render(request, 'payment/checkout.html', context)
    
    
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
                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], 
                price=item['price'])
                product_list.append(item['product'])
                
            all_products = product_list
                
            # Email order
            
            # send_mail('Order received', 'Hi! ' + '\n\n' + 'Thank you for picking your order' + '\n\n' +
            #           'Please see your order below:' + '\n\n' + str(all_products) + '\n\n' + 'Total paid: $' + 
            #           str(cart.get_all_total()), settings.EMAIL_HOST_USER, [email], fail_silently=False,)
        #     send_mail(
        #     f"New Order from {name}",
        #     f'Message:{all_products} \n {total_cost} \n {email} \n end',
        #         email,  # From email
        #         [settings.EMAIL_HOST_USER],  # To email
        #         fail_silently=False,
        # ),
        order_success = True
        response = JsonResponse({'success':order_success})
        return response
    
def payment_success(request):
    
     # Clear shopping cart
    
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
            
    return render(request, 'payment/payment-success.html')


def payment_failed(request):
    return render(request, 'payment/payment-failed.html')