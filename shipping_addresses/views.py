from django.shortcuts import render
from django.views.generic import ListView
from .models import ShippingAddress
from .forms import ShippingAddressForm

class ShippingAddressListView(ListView):
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid:
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.save()
        
    return render(request,'shipping_addresses/create.html', {
        'form':form
    })