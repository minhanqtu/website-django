"""WebsiteDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.templatetags.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/shop/', views.shop, name='shop'),
    path('home/product_detail/', views.product_detail, name='product_detail'),
    path('home/block/', views.block, name='block'),
    path('home/blocl_detail/', views.block_detail, name='block_detail'),
    path('home/cart/', views.cart, name='cart'),
    path('home/contact/', views.contact, name='contact'),
    path('home/checkout/', views.checkout, name='checkout'),
    path('home/login/', views.login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

