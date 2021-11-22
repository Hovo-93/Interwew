from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    context = {
        'product':Product.objects.all()
    }
    return render(request,'about.html',context)

def products(request):
    context = {
        'title': 'GeekShop Store',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals'},
            {'name': 'Синяя куртка The North Face'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN'},
        ]
    }
    return render(request,'shop.html',context)
