from rest_framework import viewsets

from .serializers import RoomSerializer
from  adventure.models import Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('title')
    serializer_class = RoomSerializer