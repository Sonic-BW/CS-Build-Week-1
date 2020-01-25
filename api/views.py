from rest_framework import viewsets

from .serializers import RoomSerializer, PlayerSerializer, UserSerializer
from  adventure.models import Room, Player

from django.contrib.auth.models import User


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('title')
    serializer_class = RoomSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('user')
    serializer_class = PlayerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer