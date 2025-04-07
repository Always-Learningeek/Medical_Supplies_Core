from django.shortcuts import render
from product.models import Product
from django.utils import timezone



def product_view(request):
    products = Product.objects.filter(published_at__lte=timezone.now())
    context = {'products': products}
    return render(request, 'product/shop.html', context)


def test_view(request):
    products = Product.objects.filter(published_at__lte=timezone.now())
    context = {'products': products}
    return render(request, 'product/test.html', context)