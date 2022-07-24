from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import *
from .models import *


class CreateProduct(View):
    model_form = ProductForm
    template = 'products/product_create.html'

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class UpdateProduct(View):
    # model = Product
    # model_form = ProductForm
    # template = 'products/product_update.html'

    def get(self, request, article):
        product = Product.objects.get(article__iexact=article)
        bound_form = ProductForm(instance=product)
        return render(request, 'products/product_update.html', context={'form': bound_form, 'product': product})

    def post(self, request, article):
        product = Product.objects.get(article__iexact=article)
        bound_form = ProductForm(request.POST, instance=product )

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'products/product_update.html', context={'form': bound_form, 'product': product})


class DeleteProduct(View):

    def get(self, request, article):
        product = Product.objects.get(article__iexact=article)
        return render(request, 'products/product_delete.html', context={'product': product})

    def post(self, request, article):
        product = Product.objects.get(article__iexact=article)
        product.delete()
        return redirect(reverse('products_list_url'))


def get_products_list(request):
    product = Product.objects.all()
    return render(request, 'products/product_list.html', context={'products': product})


def get_product(request, article):
    product = Product.objects.get(article=article)
    return render(request, 'products/product_page.html', context={'product': product})


def render_main_page(request):
    return render(request, 'products/main_page.html')


def add_product_cart(self):
    print(reverse('product_delete_url', kwargs={'article': self.article}))
    return reverse('product_delete_url', kwargs={'article': self.article})
