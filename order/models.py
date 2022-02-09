from django.db import models
from basket.models import Basket


class Order(models.Model):
    basket_id = ...
    total_price = models.IntegerField(null=False)
    total_price_discount = models.IntegerField(null=False)
    is_paid = models.BooleanField(null=False)
    is_finished = models.BooleanField(null=False)
