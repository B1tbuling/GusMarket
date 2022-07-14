from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from products.models import Product


def get_cart(request):
    return render(request, 'cart/cart_page.html')


def add_product_cart(request,article):
    product_cart = Product.objects.get(article=article)
    x = ProductUserСhoice.objects.filter(article=article)
    if x.name == None:
        ProductUserСhoice.objects.create(product_id=product_cart.article, amount=product_cart.amount, is_active=True)
    else:
        ProductUserСhoice.objects.update(is_active=True)
    print(product_cart.__dict__)
    print(article)
    return HttpResponse(status=201)