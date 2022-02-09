from django.urls import path
from .views import cashier_view_def

app_name = 'cashier'
urlpatterns = [
    path('', cashier_view_def),
]
