# space ship with a very basic REPL working, help command should existing and start, start should produce the error message "System error, level 2 unable to correct, trying fallback, fallback failed"

import sys
import os

def help():
    print("Commands: start, help, exit")

def start():
    print("System error, level 2 unable to correct, trying fallback, fallback failed")

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
        else:
            print("Invalid command")
    print("Goodbye")

if __name__ == "__main__":
    main()