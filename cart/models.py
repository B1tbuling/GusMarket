from django.db import models

# Create your models here.

# model: ProductUserСhoice
# form: ProductUserСhoiceForm
# table: products_users_choices


class ProductUserСhoice(models.Model):
    product_article = models.SlugField(max_length=50, null=True)
    user_id = models.IntegerField(default=1)
    order_id = models.IntegerField(default=1)
    count = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "products_users_choices"

    def __str__(self):
        return self.article


class Order(models.Model):
    user_id = models.IntegerField(default=1)
    product_article = models.SlugField(max_length=50)
    address_id = models.CharField(max_length=150)
    total_price = models.IntegerField()
    comment = models.CharField(max_length=250)
    state = models.CharField(max_length=50, default='Create')
    create_time = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(default=None, null=True)

    class Meta:
        db_table = "order"
