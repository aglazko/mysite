from django.shortcuts import render
from .models import Flat, House, Room

# Create your views here.


def place_list(request):
    # flats = []
    # for f in Flat.objects.all():
    #     flats.append(f)
    flats = Flat.objects.all()
    return render(request, 'site_app/place_list.html', {'flats': flats})