def regulate_oxygen(level, room):
    print(f"Oxygen levels are now stable at {level}% in the {room}.")

def calculate_oxygen_needed(people):
    return people * 5

def adjust_oxygen_supply(oxygen_needed):
    return oxygen_needed * 2

def find_eligible_rooms(rooms, asked_surplus):
    """
    This function determines which rooms have a safe surplus of oxygen to extract.
    Each room must have at least the asked_surplus percentage left after deduction.
    """
    safe_rooms = {}
    for room, surplus in rooms.items():
        if surplus - asked_surplus >= 5:
            safe_rooms[room] = surplus - asked_surplus
    return safe_rooms

# Example usage
rooms = {
    "Control Room": 10,
    "Engine Room": 4,
    "Storage Room": 12,
    "Living Quarters": 16
}

asked_surplus = 3
crew_count = 10

oxygen_required = calculate_oxygen_needed(crew_count)
adjusted_supply = adjust_oxygen_supply(oxygen_required)

safe_rooms = find_eligible_rooms(rooms, asked_surplus)
if safe_rooms:
    for room, remaining_surplus in safe_rooms.items():
        regulate_oxygen(remaining_surplus, room)
else:
    print("No room has a safe surplus of oxygen to extract.")

print(f"Adjusted oxygen supply needed: {adjusted_supply} units.")
