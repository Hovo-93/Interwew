from django.urls import path
from .views import index,products

app_name = 'shop'
urlpatterns = [
    path('', index, name='index'),
    path('product/',products,name='products')
]
