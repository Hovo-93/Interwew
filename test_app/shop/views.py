from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def index(request):
    context = {
        'product': Product.objects.all()
    }
    return render(request, 'about.html', context)


def products_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'products': product
    }

    return render(request, 'shop.html', context)
