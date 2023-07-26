from django.shortcuts import render
from .models import Cart
from product.models import Product
from .utils import get_or_create_cart

def cart(request):
    
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {'cart':cart})

def add(request):
    
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.product.add(product)

    return render(request, 'carts/add.html', {'product':product})