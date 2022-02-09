from django.urls import path
from .views import table_view_def

app_name = 'table'
urlpatterns = [
    path('', table_view_def)
]
