# from django.db.models.signals import post_save
from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

def generate_rooms():
    num_rooms = 115
    room_count = 0
    previous_room = None
    while room_count < num_rooms:
        if 0 <= room_count <= 9:
            room_direction = "n"
        elif 10 <= room_count <= 25:
            if room_count % 2 != 0:
                room_direction = "n"
            else:
                room_direction = "e"
        elif 26 <= room_count <= 40:
            if room_count % 2 != 0:
                room_direction = "s"
            else:
                room_direction = "e"
        elif 40 <= room_count <= 42:
            if room_count % 2 != 0:
                room_direction = "s"
            else:
                room_direction = "e"
        elif 42 <= room_count <= 57:
            if room_count % 2 != 0:
                room_direction = "n"
            else:
                room_direction = "e"
        elif  58 <= room_count <= 75:
            if room_count % 2 != 0:
                room_direction = "s"
            else:
                room_direction = "e"
        elif  76 <= room_count <= 83:
                room_direction = "s"
        elif  83 <= room_count <= 116:
                room_direction = "w"
        # Create a room in the given direction
        # room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        
        #maybe add room_count as the first field to determine id?????
        room = Room(title=f'Room {room_count}', description=f'This is room # {room_count}')
        
        
        # Note that in Django, you'll need to save the room after you create it

        # Saving the room
        room.save()
        
        # Connect the new room to the previous room
        if previous_room is not None:
            previous_room.connectRooms(room, room_direction)

        # Updating iteration variables and prev direction
        previous_room = room
        room_count += 1

players=Player.objects.all()
for p in players:
  p.currentRoom=0
  p.save()

generate_rooms()

# w = World()
# num_rooms = 115
# width = 40
# height = 20
# w.generate_rooms(width, height, num_rooms)
# w.print_rooms()


# print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
