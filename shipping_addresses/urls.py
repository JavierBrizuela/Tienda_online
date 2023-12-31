from django.urls import path
from .views import ShippingAddressListView, create

app_name = 'shipping_addresses'
urlpatterns = [
    path('', ShippingAddressListView.as_view(), name='shipping_addresses'),
    path('nuevo/', create, name='create'),
]