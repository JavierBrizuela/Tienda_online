from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from product.models import Product
from .utils import get_or_create_cart

def cart(request):
    
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {'cart':cart})

def add(request):
    
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    cuantity = request.POST.get('cuantity')
    print(cuantity)
    cart.product.add(product, through_defaults={
        'cuantity':cuantity
    })

    return render(request, 'carts/add.html', {'product':product})

def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.product.remove(product)
    return redirect('carts:cart')