from django import forms

from . import models


FlatForm = forms.modelform_factory(models.Flat, exclude=('is_approved',))
HouseForm = forms.modelform_factory(models.House, exclude=('is_approved',))
RoomForm = forms.modelform_factory(models.Room, exclude=('is_approved',))
