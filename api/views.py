from rest_framework import viewsets

from .serializers import RoomSerializer, PlayerSerializer
from  adventure.models import Room, Player


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('title')
    serializer_class = RoomSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('user')
    serializer_class = PlayerSerializer