import random
from utils import color_text, bold_text, italic_text, room_name_text, room_desc_text, item_text, command_text, error_text, success_text

# Player stats
health = 100
inventory = []
location = "Bridge"

# Items and rooms
items = ["Laser Blaster", "Medkit", "Alien Artifact", "Energy Cell", "Toolkit", "Space Helmet"]
rooms = [
    {
        "name": "Bridge",
        "description": "The command center of the ship, filled with blinking consoles and a large viewport.",
        "item": random.choice(items)
    },
    {
        "name": "Engine Room",
        "description": "The heart of the ship, humming with the sound of powerful engines.",
        "item": random.choice(items)
    },
    {
        "name": "Cargo Bay",
        "description": "A vast space filled with crates, containers, and mysterious cargo.",
        "item": random.choice(items)
    },
    {
        "name": "Med Bay",
        "description": "A sterile room with medical equipment and supplies for treating injuries.",
        "item": random.choice(items)
    }
]

commands = ["look", "move", "pick up", "attack", "inventory", "quit"]

spaceship_art = r"""
           /\
          /  \
         /----\
        /      \
       /        \
      /----------\
     /            \
    /==============\
   |      ____      |
   |     /    \     |
   |____/______\____|
      /  /  \  \
     /__/    \__\
"""

def print_room(current_room, current_room_index):
    print(f"You're in room: {room_name_text(current_room['name'])}")
    print(room_desc_text(current_room['description']))
    print(f"You see a {item_text(current_room['item'])} here.")
    for idx, room in enumerate(rooms):
        prefix = " * " if idx == current_room_index else "   "
        print(f"{prefix}{room_name_text(room['name']) if idx == current_room_index else room['name']}")

def print_help():
    print("Available commands: " + ", ".join(command_text(cmd) for cmd in commands))

def move_room(current_room_index):
    current_room_index = (current_room_index + 1) % len(rooms)
    current_room = rooms[current_room_index]
    print(f"You moved to {room_name_text(current_room['name'])}")
    print(room_desc_text(current_room['description']))
    print(f"You see a {item_text(current_room['item'])} here.")
    print("\nRooms on the ship:")
    for idx, room in enumerate(rooms):
        prefix = " * " if idx == current_room_index else "   "
        print(f"{prefix}{room_name_text(room['name']) if idx == current_room_index else room['name']}")
    return current_room_index, current_room
