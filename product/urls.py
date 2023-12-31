from django.urls import path
from .views import ProductsListView, ProductDetailView, ProductSearchListView

app_name = 'product'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('<slug>', ProductDetailView.as_view(), name='product'),
    path('search/', ProductSearchListView.as_view(), name='search'),
]