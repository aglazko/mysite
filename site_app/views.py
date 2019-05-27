import random

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models
from . import helper
from . import forms
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


@user_passes_test(helper.is_realtor, login_url='/')
def flat_create(request):
    if request.method == "POST":
        form = forms.FlatForm(request.POST, request.FILES)
        if form.is_valid():
            flat = form.save()
            models.RealtorPlacement.objects.create(realtor=request.user, flat=flat)
            return redirect(reverse(flat.get_url(), args=[flat.id]))
    else:
        form = forms.FlatForm()
    return render(request, 'site_app/flat_create.html', {'form': form})


@user_passes_test(helper.is_realtor, login_url='/')
def room_create(request):
    if request.method == "POST":
        form = forms.RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save()
            models.RealtorPlacement.objects.create(realtor=request.user, room=room)
            return redirect(reverse(room.get_url(), args=[room.id]))
    else:
        form = forms.RoomForm()
    return render(request, 'site_app/room_create.html', {'form': form})


@user_passes_test(helper.is_realtor, login_url='/')
def house_create(request):
    if request.method == "POST":
        form = forms.HouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save()
            models.RealtorPlacement.objects.create(realtor=request.user, house=house)
            return redirect(reverse(house.get_url(), args=[house.id]))
    else:
        form = forms.HouseForm()
    return render(request, 'site_app/house_create.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse(index))
    else:
        form = forms.RegistrationForm()
    return render(request, 'site_app/register.html', {'form': form})


def approve(request, type_, id):
    placements = {'rooms': models.Room, 'flats': models.Flat, 'houses': models.House}
    model = placements[type_]
    placement = get_object_or_404(model, id=id)
    placement.is_approved = True
    placement.save()
    next = request.GET.get('next')
    return redirect(next or reverse(index))
