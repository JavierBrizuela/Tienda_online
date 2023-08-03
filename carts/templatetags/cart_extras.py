from django import template

register = template.Library()

@register.filter()
def cuantity_product_format(cuantity=1):
    if cuantity==1:
        return f'{cuantity} Producto'
    return f'{cuantity} Productos'

@register.filter()
def cuantity_add_format(cuantity=1):
    add = 'agrego' if cuantity==1 else 'agregaron'
    return f'{cuantity_product_format(cuantity)} se {add}'