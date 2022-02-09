from django.db import models
from products.models import Product
from table.models import table


class BasketItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT, null=False)
    count = models.IntegerField(default=1)
    basket_id = ...


class Basket(models.Model):
    table_id = ...
    is_finish = models.BooleanField(default=False)

# Create your models here.
