from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'product': Product.on_site.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'about.html', context)


def products(request, category_id=None):
    context = {'title': 'GeekShop Products', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context['products'] = products
    return render(request, 'shop.html', context)


def products_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'products': product,
        'site': request.site,
    }
    return render(request, 'cart.html', context)
