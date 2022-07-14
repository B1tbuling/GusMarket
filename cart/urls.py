from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from .views import *

urlpatterns = [
    path('', get_cart, name='cart_page_url'),
    path('add/<str:article>', add_product_cart, name='add_product_cart_url')
]