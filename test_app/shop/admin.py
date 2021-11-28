from django.contrib import admin
from .models import Product

# admin.site.register(Product)
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'quantity', 'name_setting', 'description', 'created_timestamp')
