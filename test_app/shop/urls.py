from django.urls import path
from .views import index,products_edit

app_name = 'shop'
urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/',products_edit,name='products_edit')
]
