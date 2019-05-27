import random

from django.shortcuts import render, get_object_or_404
from . import models
from . import helper

# Create your views here.


def index(request):
    return render(request, 'site_app/index.html')


def place_list(request):
    return render(request, 'site_app/place_list.html')


# TODO: check is_auth works
def placement_list(request):
    place_types = [models.Flat, models.Room, models.House]
    filter_set = helper.get_placement_query(request)
    placements = [place for placement in place_types for place in placement.objects.filter(**filter_set)]
    random.shuffle(placements)
    return render(request, 'site_app/place_list.html', {'placements': placements})


def room_list(request):
    filter_set = helper.get_room_query(request)
    rooms = models.Room.objects.filter(**filter_set)
    return render(request, 'site_app/room_list.html', {'rooms': rooms})


def house_list(request):
    filter_set = helper.get_house_query(request)
    houses = models.House.objects.filter(**filter_set)
    return render(request, 'site_app/houses_list.html', {'houses': houses})


def flat_list(request):
    filter_set = helper.get_flat_query(request)
    flats = models.Flat.objects.filter(**filter_set)
    return render(request, 'site_app/flat_list.html', {'flats': flats})


def room_get(request, room_id):
    room = get_object_or_404(models.Room, id=room_id)
    return render(request, 'site_app/room.html', {'room': room})


def house_get(request, house_id):
    house = get_object_or_404(models.House, id=house_id)
    return render(request, 'site_app/house.html', {'house': house})


def flat_get(request, flat_id):
    flat = get_object_or_404(models.Flat, id=flat_id)
    return render(request, 'site_app/flat.html', {'flat': flat})


def flat_create(request):
    pass