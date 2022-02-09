from django.db import models


# Create your models here.
class table(models.Model):
    table_naumber = models.IntegerField(null=False, unique=True)
    position = models.CharField(max_length=2, unique=True, null=False)
    is_used = models.BooleanField(null=False)
