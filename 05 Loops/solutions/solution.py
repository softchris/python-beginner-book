import random

print("Welcome to the Alien Trap Simulator!\n")

while True:
    # Step 1: Set up the trap
    print("Step 1: Set up the trap.")
    actions = ["activate sensors", "arm lasers", "deploy net"]
    for action in actions:
        while True:
            user_input = input(f"Enter the next action ({action}): ").strip().lower()
            if user_input == action:
                break
            else:
                print("Incorrect action. Try again.")
    print("Trap successfully set up!\n")

    # Step 2: Detect the alien
    print("Step 2: Detect the alien.")
    signals = ["weak signal", "no signal", "strong signal"]
    for signal in signals:
        print(f"{signal.capitalize()} detected...")
        if signal == "strong signal":
            print("Alien is nearby!\n")
            break

    # Step 3: Capture the alien
    print("Step 3: Capture the alien.")
    commands = ["close net", "activate containment field"]
    alien_captured = True
    for command in commands:
        while True:
            user_input = input(f"Enter the next command ({command}): ").strip().lower()
            if user_input == command:
                # Random chance for alien to escape
                if random.random() < 0.2:
                    print("The alien escaped! Restarting the simulation...\n")
                    alien_captured = False
                    break
                break
            else:
                print("Incorrect command. Try again.")
        if not alien_captured:
            break

    if alien_captured:
        print("Alien captured successfully! Congratulations!\n")
        break
