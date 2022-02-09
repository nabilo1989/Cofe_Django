from django.db import models

class Category(models.Model):
    parent_id=...
    name= models.CharField(max_length=50,null=False,unique=True)
    is_sub= models.BooleanField(null=False,default=True)
