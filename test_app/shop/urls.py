from django.urls import path
from .views import index, products_edit, products

app_name = 'shop'
urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', products_edit, name='products_edit'),
    path('categories/<int:category_id>/', products, name='products')
]
