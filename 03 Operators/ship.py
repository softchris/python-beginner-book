
# space ship with a very basic REPL working, help command should existing and start, start should produce the error message "System error, level 2 unable to correct, trying fallback, fallback failed"

import sys
import os

energy_to_reroute = 50
remaining_energy = energy_to_reroute
energy_effect = 0

def display_engine_energy():
    print(f"Engine energy: {energy_effect}")

def reroute_energy(taking_energy):
    remaining_energy = energy_to_reroute - taking_energy

    engine_effect = ((taking_energy + 3) * 5) / 4

    print(f"Ship engine effect {engine_effect}, leaving {remaining_energy} behind")

def help():
    print("Commands: start, help, exit")

def start():
    print("System error, level 2 unable to correct, trying fallback, fallback failed")

def describe():
    engines = 3
    fuel_tanks = 2
    fuel_capacity = 72.5

    print(f"Engine, {engines} major engines")
    print(f"Fuel, {fuel_tanks} fuel tanks")
    print(f"Fuel capacity, {fuel_capacity} % full")

def main():
    print("Welcome to Ark-04 -- Operating system, United Earth federation")
    help()
    while True:
        command = input("Enter command: ")
        if command == "start":
            start()
        elif command == "help":
            help()
        elif command == "exit":
            break
        elif command == "describe":
            describe()
        elif command == "reroute":
            print("Available energy to reroute: ", remaining_energy)

            taking_energy = int(input("Enter energy to reroute: "))
            reroute_energy(taking_energy)

            display_engine_energy()
        elif command == "engine_energy":
            display_engine_energy()
        else:
            print("Invalid command")
    print("Goodbye")

if __name__ == "__main__":
    main()