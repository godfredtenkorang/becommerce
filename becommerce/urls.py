"""becommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from store.sitemaps import *
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from django.views.generic import RedirectView
import os


# Sitemaps
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap,
    'productpages': ProductSitemap
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="store/robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    path('users/', include('users.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('.well-known/', RedirectView.as_view(url=os.path.join(settings.BASE_DIR, '.well-known/apple-developer-merchantid-domain-association'), permanent=False)),

 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'store.views.custom_404_view'