from django.urls import path
from .views import category_view_def

app_name = 'category'
urlpatterns = [
    path('', category_view_def)
]
