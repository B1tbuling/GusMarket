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