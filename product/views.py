from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.all().order_by('-id')
    template_name = 'core/index.html'

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
        return Product.objects.filter(title=self.query())
    
    def query(self):
        return self.request.GET.get('q')