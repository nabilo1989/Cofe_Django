from django.urls import path
from .views import product_view_def

app_name = 'product'
urlpatterns = [
    path('', product_view_def)
]
