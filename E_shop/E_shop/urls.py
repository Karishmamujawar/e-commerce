"""
URL configuration for E_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name = "master"),
    path('', views.Index, name = "index"),

    path('signup', views.Signup, name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/', views.logout_view , name='logout'),

    #Add to cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    #contact url
    path('contact/',views.Contact_Page, name="contact"),
    #checkout
    path('checkout/', views.Checkout_page, name="checkout"),
    #orderpage
    path('order/', views.Your_Order,name= 'order'),
    #Product page
    path('product/', views.Product_Page , name= 'product'),
    #product details
    path('product/<str:id>', views.Product_Details, name = 'product_details'),
    #searching
    path('search/', views.Search, name = 'search'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
