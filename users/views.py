from django.shortcuts import render, redirect
from .forms import CreateUserForm
from payment.models import OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('store')
        
    context = {
        'form': form
    }
    
    
    return render(request, 'users/registration/register.html', context)




@login_required
def track_orders(request):
    try:
        orders = OrderItem.objects.filter(user=request.user)
        context = {'orders':orders, 'title':'Track orders'}
        return render(request, 'users/track-orders.html', context=context)
    
    except:
        return render(request, 'users/track-orders.html')