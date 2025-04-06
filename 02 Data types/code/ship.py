# space ship with a very basic REPL working, help command should existing and start, start should produce the error message "System error, level 2 unable to correct, trying fallback, fallback failed"

import sys
import os

def help():
    print("Commands: start, help, exit, ship")

def start():
    print("System error, level 2 unable to correct, trying fallback, fallback failed")

def ship():
    engines = 3  # integer, major engines
    fuel_tanks = 2  # integer, number of fuel tanks
    fuel_capacity_percentage = 72.5  # float, percentage full
    print("Ship details:")
    print(f"\t- {engines} major engines.")
    print(f"\t- The ship is equipped with {fuel_tanks} fuel tanks.")
    print(f"\t- The fuel tanks are {fuel_capacity_percentage}% full.")

def main():
    print("Welcome to Ark-04 -- Operating system, United Earth federation")
    help()
    while True:
        command = input("Enter command: ")
        if command == "start":
            start()
        elif command == "help":
            help()
        elif command == "ship":
            ship()
        elif command == "exit":
            break
        else:
            print("Invalid command")
    print("Goodbye")

if __name__ == "__main__":
    main()