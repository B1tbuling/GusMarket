from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from .views import *

def test(request):
    print('ffffffff')
    return HttpResponse(status=200)

urlpatterns = [
    path('', render_main_page, name='main_page_url'),
    path('list/', get_products_list, name='products_list_url'),
    path('products/create', CreateProduct.as_view(), name='product_create_url'),
    path('products/<str:article>/delete', DeleteProduct.as_view(), name='product_delete_url'),
    path('products/<str:article>/update/', UpdateProduct.as_view(), name='product_update_url'),
    path('products/<str:article>', get_product, name='product_url')
]