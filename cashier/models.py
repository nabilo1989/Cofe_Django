from django.db import models


class Cashier(models.Model):
    username = models.CharField(max_length=40, null=False, unique=True)
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    phone_number = models.IntegerField(null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=20, null=False)
