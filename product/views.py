from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Product

class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.all().order_by('-id')
    template_name = 'index.html'

    def get_context_data(self, **kward):
        context = super().get_context_data(**kward)
        context['message'] = 'Listado de productos'
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'

class ProductSearchListView(ListView):
    model = Product
    template_name = 'product/search.html'
    
    def get_queryset(self):
        filter = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Product.objects.filter(filter)
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query']= self.query()
        context['quantity'] = context['product_list'].count()
        return context