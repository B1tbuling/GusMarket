from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from products.models import Product


def add_product_cart(request, article):
    x = ProductUserСhoice.objects.filter(product_article=article).first()
    if x is None:
        print('tut')
        product_cart = Product.objects.get(article=article)
        ProductUserСhoice.objects.create(product_article=product_cart.article, count=product_cart.amount,
                                         is_active=True)
    else:
        print('netut')
        ProductUserСhoice.objects.filter(product_article=article).update(is_active=False)
    return HttpResponse(status=201)


def get_products_list_in_cart(request):
    m = []
    list_cart = []

    products_carts = ProductUserСhoice.objects.all()
    for p in products_carts:
        m.append(p.product_article)

    products = Product.objects.filter(article__in=m)
    for product in products:
        for cart in products_carts:
            if product.article == cart.product_article:
                list_cart.append((product, cart))
                break

    return render(request, 'cart/cart_page.html', context={'list_cart': list_cart})


def delete_product_cart(request, article):
    print(article)
    product_delete = ProductUserСhoice.objects.get(product_article__iexact=article)
    product_delete.delete()
    return redirect(reverse('cart_page_url'))

def get_order_cart(request):
    m = []
    list_cart = []

    products_carts = ProductUserСhoice.objects.all()
    for p in products_carts:
        m.append(p.product_article)

    products = Product.objects.filter(article__in=m)
    for product in products:
        for cart in products_carts:
            if product.article == cart.product_article:
                list_cart.append((product, cart))
                break

    return render(request, 'cart/cart_page.html', context={'list_cart': list_cart})