from game import health, inventory, location, items, rooms, commands, spaceship_art, print_room, print_help, move_room
from utils import success_text, error_text

def main():
    print("Welcome aboard the Starship Python!")
    print(f"You are in the {location}. Health: {health}")
    print(spaceship_art)

    current_room_index = 0
    current_room = rooms[current_room_index]
    print_room(current_room, current_room_index)

    while health > 0:
        print("What do you want to do? Type 'help' for options")
        command = input("Command> ").strip().lower()
        if command == "help":
            print_help()
        elif command == "look":
            print_room(current_room, current_room_index)
        elif command == "move":
            current_room_index, current_room = move_room(current_room_index)
        elif command == "quit":
            print(success_text("Thank you for playing!"))
            break
        else:
            print(error_text(f"Unknown command: {command}"))

if __name__ == "__main__":
    main()