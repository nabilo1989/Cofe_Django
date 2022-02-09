from django.shortcuts import render
from django.views import View


def index_view(request):
    return render(request, 'core/index.html')