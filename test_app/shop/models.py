from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=256)
    name_setting = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    category1 = models.ManyToManyField(ProductCategory, related_name='category1')

    def __str__(self):
        return f'{self.name_product}| {self.category.name}'