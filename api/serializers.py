from rest_framework import serializers

from adventure.models import Room, Player

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('title', 'description', 'n_to','s_to','e_to','w_to')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('user', 'currentRoom', 'uuid')