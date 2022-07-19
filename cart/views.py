from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from products.models import Product


# def get_cart(request):
#     return render(request, 'cart/cart_page.html')


def add_product_cart(request, article):
    x = ProductUserСhoice.objects.filter(product_article=article).first()
    if x is None:
        print('tut')
        product_cart = Product.objects.get(article=article)
        ProductUserСhoice.objects.create(product_article=product_cart.article, count=product_cart.amount, is_active=True)
    else:
        print('netut')
        ProductUserСhoice.objects.update(is_active=True)
    return HttpResponse(status=201)


def get_products_list_in_cart(request):
    product_curt = ProductUserСhoice.objects.all()
    m = []
    product_dict = []
    cart_dict = []
    cart = []
    cart_all = []

    product_curt = ProductUserСhoice.objects.all()
    for p in product_curt:
        m.append(p.product_article)
    product = Product.objects.filter(article__in=m)

    for p in product:
        product_dict.append([p.article, p.name, p.price, p.amount])

    for p in product_curt:
        cart.append([p.count, p.is_active])

    for i in range(len(product_dict)):
        cart_all.append(product_dict[i] + cart[i])

    return render(request, 'cart/cart_page.html', context={'cart_all': cart_all})
