from django.db import models


# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=256)
    name_setting = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
