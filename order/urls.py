from django.urls import path
from .views import order_view_def

app_name = 'order'
urlpatterns = [
    path('', order_view_def)
]
