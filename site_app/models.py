import os

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_realtor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


def get_file_path(instance, filename, folder=""):
    return os.path.join(instance.__class__.__name__.lower(), folder, filename)


def get_image_path(instance, filename):
    return get_file_path(instance, filename, 'images')


class Placement(models.Model):
    class Meta:
        abstract = True
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    cost = models.IntegerField()
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=get_image_path, blank=True, default='default.png')
    owner_contract = models.FileField(upload_to=get_file_path, blank=True)
    is_free = models.BooleanField(default=True)
    end_date = models.DateField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __repr__(self):
        return self.heading

    def get_url(self):
        return '{}_get'.format(self.__class__.__name__.lower())


class Room(Placement):
    size = models.IntegerField()
    floor = models.IntegerField()
    total_rooms = models.IntegerField()
    elevator = models.BooleanField(default=False)


class Flat(Placement):
    total_size = models.IntegerField()
    living_size = models.IntegerField()
    kitchen_size = models.IntegerField()
    rooms_count = models.IntegerField()
    floor = models.IntegerField()
    elevator = models.BooleanField(default=False)


class House(Placement):
    house_size = models.IntegerField()
    garage = models.BooleanField(default=False)
    outdoors_size = models.IntegerField()


class RealtorPlacement(models.Model):
    id = models.AutoField(primary_key=True)
    realtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='realtor')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    placement = models.ForeignKey(RealtorPlacement, on_delete=models.CASCADE, related_name="placement")
    placement_type = models.CharField(max_length=25)
    is_approved = models.BooleanField(default=False)

    def get_placement(self):
        return getattr(self.placement, self.placement_type)

    def get_approve_url(self):
        return 'contracts/{}/approve'.format(self.id)

class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=500)
