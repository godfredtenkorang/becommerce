from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from payment.models import OrderItem
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


# Create your views here.
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            
            # Email verification setup (template)
            
            current_site = get_current_site(request)
            subject = 'Account verification email'
            message = render_to_string('users/registration/email-verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })
            
            user.email_user(subject=subject, message=message)
            
            return redirect('email-verification-sent')
        
    context = {
        'form': form,
        
    }
    
    
    return render(request, 'users/registration/register.html', context)



@login_required(login_url='my-login')
def track_orders(request):
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
    
    messages.success(request, "Logout success")
    
    return redirect('index')