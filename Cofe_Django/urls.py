from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls', namespace='basket')),
    path('cashier/', include('cashier.urls', namespace='cashier')),
    path('order/', include('order.urls', namespace='order')),
    path('table/', include('table.urls', namespace='table')),
    path('products/',include('products.urls',namespace='products')),

]
