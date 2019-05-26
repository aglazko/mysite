from django.shortcuts import render
from .models import Flat, House, Room

# Create your views here.


def index(request):
    return render(request, 'site_app/index.html')


def place_list(request):
    return render(request, 'site_app/place_list.html')