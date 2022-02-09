from django.urls import path
from .views import basket_view_def

app_name = 'basket'
urlpatterns = [
    path('', basket_view_def)
]
