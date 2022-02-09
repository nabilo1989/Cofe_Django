from django.db import models
from category.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    category_id = ...
    discount = models.IntegerField(default=0)
    img = models.ImageField(null=True)
