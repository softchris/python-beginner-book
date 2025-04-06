def find_room_with_surplus(rooms, asked_surplus):
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
safe_rooms = find_room_with_surplus(rooms, asked_surplus)
if safe_rooms:
    for room, remaining_surplus in safe_rooms.items():
        print(f"We can safely extract {asked_surplus}% oxygen from the {room}. Remaining surplus: {remaining_surplus}%.")
else:
    print("No room has a safe surplus of oxygen to extract.")