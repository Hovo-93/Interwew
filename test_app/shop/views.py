from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    context = {
        'product':Product.objects.all()
    }
    return render(request,'about.html',context)

def products(request):

    return render(request,'shop.html')
