# A space game

import random

# Player stats
health = 100
inventory = []
location = "Bridge"

# Rooms
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

print("Welcome aboard the Starship Python!")
print(f"You are in the {location}. Health: {health}")


current_room_index = 0
current_room = rooms[current_room_index]
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
print(spaceship_art)
print(f"You're in room: \033[1m{current_room['name']}\033[0m")
print(f"\033[93m\033[3m{current_room['description']}\033[0m")
print(f"You see a \033[92m{current_room['item']}\033[0m here.")

while health > 0:
    print("What do you want to do? Type 'help' for options")
    command = input("Command> ").strip().lower()
    if command == "help":
        print("Available commands: " + ", ".join(f"\033[94m{cmd}\033[0m" for cmd in commands))
    elif command == "look":
        print(f"You're in \033[1m{current_room['name']}\033[0m\n\033[93m\033[3m{current_room['description']}\033[0m")
        print(f"You see a \033[92m{current_room['item']}\033[0m here.")
    elif command == "move":
        current_room_index = (current_room_index + 1) % len(rooms)
        current_room = rooms[current_room_index]
        print(f"You moved to \033[1m{current_room['name']}\033[0m")
        print(f"\033[93m\033[3m{current_room['description']}\033[0m")
        print(f"You see a \033[92m{current_room['item']}\033[0m here.")
    elif command == "quit":
        print("\033[92mThank you for playing!\033[0m")
        break
    else:
        print(f"\033[91mUnknown command: {command}\033[0m")