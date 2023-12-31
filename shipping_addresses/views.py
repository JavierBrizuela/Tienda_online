from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ShippingAddress
from .forms import ShippingAddressForm
from django.contrib import messages

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
        shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists()
        shipping_address.save()

        messages.success(request, 'La direccion se creo correctamente')
        return redirect('shipping_addresses:shipping_addresses')

    return render(request,'shipping_addresses/create.html', {
        'form':form
    })