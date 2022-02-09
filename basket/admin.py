from django.contrib import admin
from basket.models import Basket
from basket.models import BasketItem


admin.site.register(Basket)
admin.site.register(BasketItem)