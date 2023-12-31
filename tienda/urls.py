
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('users/', include('users.urls') ),
    path('carrito/', include('carts.urls') ),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)