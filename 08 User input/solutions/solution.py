from datetime import datetime

def send_to_mainframe(data, user, timestamp):
    # Simulate sending data to the ship's mainframe
    print(f"Sending data to mainframe: {data}")
    print(f"Recorded by: {user} at {timestamp}")

# Ask for the user's name
user_name = input("Enter your name: ").strip()

# Helper function to get sensor values
def get_sensor_value(sensor_number):
    """
    Prompts the user to input a value for a specific sensor.

    Parameters:
    sensor_number (int): The sensor number (1, 2, or 3).

    Returns:
    int/float/bool: The value entered by the user, converted to the appropriate type.
    """
    while True:
        try:
            if sensor_number == 1:
                return int(input("Enter a whole number: ").strip())
            elif sensor_number == 2:
                return float(input("Enter a decimal number: ").strip())
            elif sensor_number == 3:
                value = int(input("Enter a boolean value (0 or 1): ").strip())
                if value in [0, 1]:
                    return bool(value)
                else:
                    print("Error: Please enter 0 or 1.")
        except ValueError:
            print("Error: Invalid input. Please try again.")

# Collect and send values from the sensors using a loop

for sensor_number in range(1, 4):
    sensor_data = get_sensor_value(sensor_number)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send_to_mainframe({f"sensor{sensor_number}": sensor_data}, user_name, current_time)