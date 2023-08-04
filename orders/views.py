from django.shortcuts import render
from carts.utils import get_or_create_cart
from orders.utils import get_or_create_order

def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request, cart)
    

    return render(request, 'orders/order.html', {})
