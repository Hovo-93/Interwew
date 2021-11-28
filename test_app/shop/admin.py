from django.contrib import admin
from .models import Product, ProductCategory


# admin.site.register(Product)
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'quantity', 'name_setting', 'description', 'created_timestamp','category')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
