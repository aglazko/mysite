import random
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models
from . import helper
from . import forms
# Create your views here.

PLACEMENTS = {'rooms': models.Room, 'flats': models.Flat, 'houses': models.House}

def index(request):
    return render(request, 'site_app/index.html')


def place_list(request):
    return render(request, 'site_app/place_list.html')


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
    if not room.is_approved:
        if (request.user.is_authenticated and not (request.user.is_admin or request.user.is_realtor)) or not request.user.is_authenticated:
            raise Http404
    return render(request, 'site_app/room.html', {'room': room})


def house_get(request, house_id):
    house = get_object_or_404(models.House, id=house_id)
    if not house.is_approved:
        if (request.user.is_authenticated and not (request.user.is_admin or request.user.is_realtor)) or not request.user.is_authenticated:
            raise Http404
    return render(request, 'site_app/house.html', {'house': house})


def flat_get(request, flat_id):
    flat = get_object_or_404(models.Flat, id=flat_id)
    if not flat.is_approved:
        if (request.user.is_authenticated and not (request.user.is_admin or request.user.is_realtor)) or not request.user.is_authenticated:
            raise Http404
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


@user_passes_test(lambda user: user.is_admin, login_url='/')
def approve(request, type_, id):
    model = PLACEMENTS[type_]
    placement = get_object_or_404(model, id=id)
    placement.is_approved = True
    placement.save()
    next = request.GET.get('next')
    return redirect(next or reverse(index))


@user_passes_test(lambda user: not user.is_authenticated, login_url='/')
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


@login_required
def profile(request):
    instance = get_object_or_404(models.User, id=request.user.id)
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse(index))
    else:
        form = forms.ProfileForm(instance=request.user)
    return render(request, 'site_app/profile.html', {'form': form})


@user_passes_test(helper.is_realtor, '/')
def room_update(request, id):
    room = get_object_or_404(models.Room, id=id)
    if request.method == "POST":
        form = forms.RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect(reverse(room.get_url(), args=[room.id]))
    else:
        form = forms.RoomForm(instance=room)
    return render(request, 'site_app/room_create.html', {'form': form})


@user_passes_test(helper.is_realtor, '/')
def flat_update(request, id):
    flat = get_object_or_404(models.Flat, id=id)
    if request.method == "POST":
        form = forms.FlatForm(request.POST, request.FILES, instance=flat)
        if form.is_valid():
            form.save()
            return redirect(reverse(flat.get_url(), args=[flat.id]))
    else:
        form = forms.FlatForm(instance=flat)
    return render(request, 'site_app/flat_create.html', {'form': form})


@user_passes_test(helper.is_realtor, login_url='/')
def house_update(request, id):
    house = get_object_or_404(models.House, id=id)
    if request.method == "POST":
        form = forms.HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect(reverse(house.get_url(), args=[house.id]))
    else:
        form = forms.HouseForm(instance=house)
    return render(request, 'site_app/house_create.html', {'form': form})


@user_passes_test(helper.is_normal_user, login_url='/')
def contract_list(request):
    contracts = models.Contract.objects.filter(user=request.user)
    return render(request, 'site_app/contract_list.html', {'contracts': contracts})


@user_passes_test(lambda user: user.is_realtor, login_url='/')
def realtor_contract_list(request):
    contracts = models.Contract.objects.filter(placement__realtor__username=request.user)
    return render(request, 'site_app/realtor_contract_list.html', {'contracts': contracts})


@user_passes_test(helper.is_normal_user, login_url='/')
def contract_create(request, type_, id):
    model = PLACEMENTS[type_]
    place = get_object_or_404(model, id=id)
    placement_type = type_.lower()
    mapper = get_object_or_404(models.RealtorPlacement, **{placement_type: place})
    models.Contract.create(user=request.user, placement=mapper, placement_type=placement_type)
    return redirect(reverse(contract_list))


@user_passes_test(lambda user: user.is_realtor, login_url='/')
def contract_approve(request, id):
    contract = get_object_or_404(models.Contract, id=id)
    contract.is_approved = True
    contract.save()
    return redirect(reverse(realtor_contract_list))
