from rest_framework import serializers

from adventure.models import Room, Player
from django.contrib.auth.models import User

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'title', 'description', 'n_to','s_to','e_to','w_to')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'user', 'currentRoom', 'uuid')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'is_superuser')