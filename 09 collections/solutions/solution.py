readings = {}

while True:
    print("Commands: list, add, update, exit")
    command = input("Enter command: ")

    if command == "list":
        print("Readings from the arkship:")
        for key, value in readings.items():
            print(key + ":", value)
    elif command == "add":
        key = input("Enter key: ")
        value = input("Enter value: ")
        readings[key] = value
    elif command == "update":
        key = input("Enter key to update: ")
        if key in readings:
            value = input("Enter new value: ")
            readings[key] = value
        else:
            print("Key not found")
    elif command == "exit":
        break
    else:
        print("Invalid command")