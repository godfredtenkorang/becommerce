from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from payment.models import OrderItem, ShippingAddress
from payment.forms import ShoppingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site

from .token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from store.models import Newsletter

from django.core.mail import send_mail

from django.conf import settings


# Create your views here.
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            
            return redirect('my-login')

            
            # Email verification setup (template)
            
            # current_site = get_current_site(request)
            # subject = 'Account verification email'
            # message = render_to_string('users/registration/email-verification.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': user_tokenizer_generate.make_token(user),
            # })
            
            # user.email_user(subject=subject, message=message)
            
            # return redirect('email-verification-sent')
        
            
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'form': form,
        'title': 'Register'
    }
    
    
    return render(request, 'users/registration/register.html', context)


@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'users/dashboard.html', {'title':'Dashboard'})


@login_required(login_url='my-login')
def profile_management(request):
    user_form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.info(request, "Your account has been updated")
            return redirect('dashboard')
        
    context = {
        'user_form': user_form,
        'title': 'Profile Management'
    }
    return render(request, 'users/profile-management.html', context=context)


@login_required(login_url='my-login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        messages.info(request, "Your account has been deleted")
        return redirect('index')
    return render(request, 'users/delete-account.html', {'title':"Delete account"})




# Shipping View
@login_required(login_url='my-login')
def manage_shipping(request):
    try:
        # Account user with shipping information
        shipping = ShippingAddress.objects.get(user=request.user.id)
        
    except ShippingAddress.DoesNotExist:
        # Account user with no shipping information
        shipping = None
        
    form = ShoppingForm(instance=shipping)
    
    if request.method == 'POST':
        form = ShoppingForm(request.POST, instance=shipping)
        if form.is_valid():
            # Assign the user FK on the object
            
            shipping_user = form.save(commit=False)
            shipping_user.user = request.user
            
            shipping_user.save()
            messages.success(request, 'Your shipping address has been updated successfully')
            return redirect('manage-shipping')
    
    context = {
        'form': form,
        'title': 'Manage shipping'
    }
    return render(request, 'users/manage-shipping.html', context=context)


@login_required(login_url='my-login')
def track_orders(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    try:
        orders = OrderItem.objects.filter(user=request.user)
        context = {'orders':orders, 'title':'Track orders'}
        return render(request, 'users/track-orders.html', context=context)
    
    except:
        return render(request, 'users/track-orders.html')
    
    
def email_verification(request, uidb64, token):
    # uniqueid
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)
    
    # Success
    
    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('email-verification-success')
    
    
    # Failed
    else:
        return redirect('email-verification-failed')

def email_verification_sent(request):
    return render(request, 'users/registration/email-verification-sent.html', {'title':'Email verifivation sent'})


def email_verification_success(request):
    return render(request, 'users/registration/email-verification-success.html', {'title': 'Email verifivation succes'})



def email_verification_failed(request):
   return render(request, 'users/registration/email-verification-failed.html', {'title': 'Email verifivation failed'})


# login

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have logged in successfully")
                return redirect("index")
            
    context = {
        'form': form,
        'title': "Login"
    }
        
    return render(request, 'users/my-login.html', context=context)


# logout


def user_logout(request):
    
    try:
        for key in list(request.session.keys()):
            if key == 'session_key':
                continue
            else:
                del request.session[key]
    except KeyError:
        pass
    
    messages.success(request, "You have logged out successfully")
    
    return redirect('index')