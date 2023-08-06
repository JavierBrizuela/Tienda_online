from .models import Order
from django.urls import reverse

def get_or_create_order(request, cart):
    
    order = cart.order
    
    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)

    if order:
        request.session['order_id'] = order.order_id
    return order

def breadcrumb(product=True, addres=False, payment=False, confirmation=False):
    return [
        {'title':'productos', 'active':product, 'url': reverse('orders:order')},
        {'title':'direccion', 'active':addres, 'url': reverse('orders:order')},
        {'title':'pagos', 'active':payment, 'url': reverse('orders:order')},
        {'title':'confirmacion', 'active':confirmation, 'url': reverse('orders:order')},
    ]