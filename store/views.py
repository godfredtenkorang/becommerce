from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from django.db.models import Q # New
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    laptopshops = LaptopsAndTablet.objects.all()
    applesytems = AppleSystem.objects.all()
    gaminglaptops = GamingLaptops.objects.all()
    accessories = ComputerAccessories.objects.all()
    components = ComponentsAndParts.objects.all()
    surviellences = SurveillanceSystems.objects.all()
    heels = HeelsAndSlippers.objects.all()
    shoes = ShoesAndSlippers.objects.all()
    banners = Banner.objects.all()
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        send_mail(
        f"New Subscriber from {email}",
        f'{email} \n end',
            email,  # From email
            [settings.EMAIL_HOST_USER],  # To email
            fail_silently=False,
    ),
        return redirect('index')
    context = {
        'laptopshops': laptopshops,
        'applesytems': applesytems,
        'gaminglaptops': gaminglaptops,
        'accessories': accessories,
        'components': components,
        'surviellences': surviellences,
        'heels': heels,
        'shoes': shoes,
        'banners': banners
    }
    return render(request, 'store/index.html', context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def productDetail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    context = {
        'product': product
    }
    return render(request, 'store/details/productDetail.html', context)

# def shopDetail(request, shop_slug):
#     shop = get_object_or_404(Shop, slug=shop_slug)
    
#     context = {
#         'shop': shop
#     }
#     return render(request, 'store/shopDetail.html', context)

def shop(request):
    shops = Product.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
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
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    context = {
        'search': search,
        'search_item': search_item
    }
    return render(request, 'store/search.html', context)



def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    
    products = Product.objects.filter(category=category)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'category': category,
        'products': products,
        'title': 'Categories'
    }
    return render(request, 'store/list-category.html', context)


# All Home Details

def laptopsandtablet(request, laptops_slug):
    laptop = get_object_or_404(LaptopsAndTablet, slug=laptops_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'laptop': laptop
    }
    return render(request, 'store/details/laptopsDetail.html', context)


def applesytem(request, apple_slug):
    apple = get_object_or_404(AppleSystem, slug=apple_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'apple': apple,
    }
    return render(request, 'store/details/appleDetails.html', context)


def gaminglaptop(request, gaming_slug):
    gaming = get_object_or_404(GamingLaptops, slug=gaming_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'gaming': gaming,
    }
    return render(request, 'store/details/gamingDetails.html', context)

def computer_accessories(request, accessory_slug):
    accessory = get_object_or_404(ComputerAccessories, slug=accessory_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'accessory': accessory,
    }
    return render(request, 'store/details/AccessoryDetails.html', context)


def component_and_parts(request, component_slug):
    component = get_object_or_404(ComponentsAndParts, slug=component_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'component': component,
    }
    return render(request, 'store/details/componentsDetails.html', context)


def surviellence_systems(request, surviellence_slug):
    surviellence = get_object_or_404(SurveillanceSystems, slug=surviellence_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'surviellence': surviellence,
    }
    return render(request, 'store/details/surviellenceDetails.html', context)


def heelsandslippers(request, heels_slug):
    heels = get_object_or_404(SurveillanceSystems, slug=heels_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'heels': heels,
    }
    return render(request, 'store/details/heelsDetails.html', context)


def shoesandslippers(request, shoe_slug):
    shoe = get_object_or_404(ShoesAndSlippers, slug=shoe_slug)
    
    if request.method == 'POST':
        email = request.POST['email']
        
        newletter = Newsletter(email=email)
        newletter.save()
        return redirect('index')
    
    context = {
        'shoe': shoe,
    }
    return render(request, 'store/details/shoesDetails.html', context)


def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()
        
        messages.success(request, 'Your form has been sent successfully. You will hear from us soon!')
        
        send_mail(
        f"New Subscriber from {name}",
        f'{email} \n\n {phone} \n\n {subject} \n\n {message}',
            email,  # From email
            [settings.EMAIL_HOST_USER],  # To email
            fail_silently=False,
        ),
        
        return redirect('contactUs')
        
    return render(request, 'store/contactUs.html')

def faQ(request):
    return render(request, 'store/faq.html')

def terms(request):
    return render(request, 'store/termscondi.html')
