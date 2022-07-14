from time import time
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class Product(models.Model):
    article = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=150)
    price = models.FloatField(db_index=True)
    amount = models.IntegerField(db_index=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "products"

    def get_absolute_url(self):
        return reverse('product_url', kwargs={'article': self.article})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'article': self.article})


    def get_delete_url(self):
        return reverse('product_delete_url', kwargs={'article': self.article})


    def __str__(self):
        return self.article