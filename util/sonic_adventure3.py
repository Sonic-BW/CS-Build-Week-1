from  django.contrib.auth.models import User
from adventure.models import Player, Room
from random import randrange

Room.objects.all().delete()

#while loop

#class World:

def geck(self, num_rooms):
    room_count = 0
    direction = None
    prev_room = None
    curr_room = None

    while room_count < num_rooms:
        room_attacher = randrange(4)
        direction = randrange(12)
        if direction <= 3 and room_attacher % 2 == 0:
            room_dir = "n"
            
        elif 3 < direction <= 6:
            room_dir = "e"
            
        elif 6 < direction <= 9:
            room_dir ="s"
            
        else:
            room_dir ="w"
           

        room = Room(room_count, "A room", "run through lambhog")

        if prev_room is not None:
            prev_room.connectRooms(curr_room, room_dir)

        prev_room = curr_room
        room_count += 1
