import random

# Define actions as strings
actions = [
    "Set up trap",
    "Lure alien with food",
    "Activate motion sensors",
    "Close containment door"
]

alien_caught = False

for action in actions:
    # Assign a random outcome (True/False) for each action
    action_outcome = random.choice([True, False])
    print(f"Action: {action} executed. Outcome: {action_outcome}")
    alien_caught = action_outcome
    # Update alien_caught based on the action outcome
    if alien_caught == True:
      print(f"[Alien caught!!] using: {action}")
      break
    else:
      print("Alien not caught yet, proceeding to the next action...")

if not alien_caught:
    print("The alien escaped! We'll need a better plan next time.")
