from django.shortcuts import render, redirect
from .forms import CreateUserForm

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