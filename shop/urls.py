"""Ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name= 'shop'

urlpatterns = [
    path('',views.Product_List.as_view(),name='product_list'),
    path('addtocart/<slug:slug>/',views.addtocart,name='addtocart'),
    path('cartlist',views.cartlist.as_view(),name='cartlist'),
    path('remove_from_cart/<slug:slug>/',views.remove_product_from_cart,name='remove_from_cart'),
    path('create_product/<slug:slug>/',views.CreateProduct,name='create_product'),
    path('order_list/',views.OrderList.as_view(),name='order_list'),
    path('cancel_order/<slug:slug>/<int:pk>',views.CancelOrder,name='cancelorder'),
    path('searchquery/',views.searchquery,name='searchquery'),
    path('final_order/<slug:slug>/<int:pk>',views.final_order,name='final_order'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

