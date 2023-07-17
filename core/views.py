from django.shortcuts import render
from product.models import Product
# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'core/index.html', {'products':products})