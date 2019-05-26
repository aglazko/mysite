from django.contrib import admin
from .models import House, Flat, Room, User

# Register your models here.


admin.site.register(House)
admin.site.register(Flat)
admin.site.register(Room)
admin.site.register(User)
