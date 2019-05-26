from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import House, Flat, Room, RealtorPlacement, Contract, PrivateMessage

# Register your models here.
User = get_user_model()

admin.site.register(House)
admin.site.register(Flat)
admin.site.register(Room)
admin.site.register(User)
admin.site.register(RealtorPlacement)
admin.site.register(Contract)
admin.site.register(PrivateMessage)
