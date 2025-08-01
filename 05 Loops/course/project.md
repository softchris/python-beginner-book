# A space game

Let's create a space game based on what we learned so far on variables, types and operators.

## Game Concept:

- The player is an astronaut on a spaceship.
- The spaceship has different rooms (bridge, engine room, cargo bay, etc.).
- The player can move between rooms, check their status (health, inventory), and interact with simple events (fix engine, find items).
- Use variables for player stats, room states, and inventory.
- Use types (int, str, list) for stats, room names, and inventory.
- Use operators for actions (add/remove items, health changes).

## Sample Game Flow:

- Start in the bridge. Show player stats.
- Let the player choose where to go (input).
- In each room, random events can happen (using operators to change stats).
- Win by fixing the ship or collecting all items.

## Starting code

```python
import random

# Player stats
health = 100
inventory = []
location = "Bridge"

# Rooms
rooms = ["Bridge", "Engine Room", "Cargo Bay", "Med Bay"]
action = ["move", "inventory", "attack", "pick up", "look"], 

print("Welcome aboard the Starship Python!")
print(f"You are in the {location}. Health: {health}")

while health > 0:
    print("What do you want to do?")
    action = input("Action> ").strip().lower()
    # Carry out action if valid
```