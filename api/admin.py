from django.contrib import admin
from adventure.models import Room, Player
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Room)
admin.site.register(Player)
admin.site.register(User)

