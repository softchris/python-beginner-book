# Loops, iterating over many elements

It's common in programming that you need to repeat a set of instructions multiple times. You could for example be working on a dataset representing rows in a file or queue where you need to process each item. In Python, there are various constructs to support having do redo a set of instructions.

## Introduction

In this chapter we will:

- Use for-loops to repeat instructions and iterate over a dataset.
- Leverage a while-loop for repeating a set of instructions.
- Apply functions like `range`, `enumerate`, `zip` and list comprehensions to construct and iterate over a dataset.

## Narrative: Friendly Intruder

_While investigating a strange noise, Tabitha stumbles upon a mischievous little alien poking around the hydroponics bay. The creature seems friendly enough, but it has a knack for getting into all the wrong places—like the wiring she’s desperately trying to repair. It’s a game of cat and mouse, with Tabitha trying to outsmart the curious intruder before it causes more chaos!_

<div>
    <img src="./assets/hydroponics.jpeg" alt="Hydroponics bay" width="600">
</div>

## while, repeat until meeting a condition

**Ship**: Tabitha, I detect an intruder in the hydroponics bay. You need to catch it before it causes more damage.

**Tabitha**: What do you mean intruder, specify?

**Ship**: It looks like an alien life form, it's curious and keeps poking around the wiring. You need to catch it before it causes more damage.

**Tabitha**: Wow, what's the protocol here, we know nothing about it right?

**Ship**: Correct, we need to catch it and study it, using extreme precaution. In fact, we might need to construct a program that can catch it. We need to learn about the alien's behavior and how to catch it. In fact, let's study up on loops, as we might need to repeat a set of instructions until we catch it.

A `while` construct allows us to repeat something a number of times. Some examples of this behavior are:

- **a command line program where you read user input**, carry out a command and then waiting for the user to type again:

   ```text
   type a command: help
   printing commands
   help, shows available command
   list, shows all order records
   print, prints order records to a file

   type a command: 
   ```

- **read data**. There are many data sources that you need to read data from and you don't know when it will end like reading a data stream over a network for example.

For both of these examples, a `while` construct is good to use and your code can look something like so:

```python
while <some condition>:
  # read command
  # perform a task
```

**Tabitha**: I see, so for our "alien catcher" program, makes sense.

### Example of using `while`

Let's look at a few examples of using `while` so we understand the mechanics behind it:

```python
alien_caught = False
attempts = 0

while not alien_caught and attempts < 10:
    print(f"Attempt {attempts + 1}: Searching for the alien...")
    # Simulate finding the alien on the 7th attempt
    if attempts == 6:
        print("Alien caught!")
        alien_caught = True
    else:
        print("Alien not found, trying again...")
    attempts += 1
```

The above code simulates trying to catch an alien aboard a spaceship. Key points of the code are:

- **Condition**, `not alien_caught and attempts < 10`: The loop continues until the alien is caught or the maximum number of attempts (10) is reached.
- **Incrementation step**, `attempts += 1`: This ensures the number of attempts increases with each iteration, preventing an infinite loop.
- **Alien-catching logic**, `if attempts == 6`: Simulates catching the alien on the 7th attempt.
- **Output**, `print(...)`: Provides feedback on each attempt to locate the alien.

**Ship**: Of course, the alien won't be caught this easily, we need to be more creative.

### Use `break` and `continue` to control the loop behavior

**Ship**: We need more control when working with loops, so that we can stop the loop when we want or skip a step. We can use `break` and `continue` to control the loop. See below how we can update our code to use `break` and `continue`:

```python
alien_caught = False
attempts = 0

while attempts < 10:
    print(f"Attempt {attempts + 1}: Searching for the alien...")
    # Simulate skipping certain attempts
    if attempts % 2 == 0:
        print("Skipping this attempt...")
        attempts += 1
        continue
    # Simulate finding the alien on the 7th attempt
    if attempts == 6:
        print("Alien caught!")
        alien_caught = True
        break
    else:
        print("Alien not found, trying again...")
    attempts += 1
```

How it works:

- `break` stops the loop when the alien is caught instead of continuing to the maximum number of attempts.
- `continue` skips certain attempts, in this case every second attempt, to simulate a more realistic search.

**Tabitha**: I see, so we can use `break` to stop the loop and `continue` to skip a step and `while` to repeat a set of instructions until a condition is met.

## Using `for`

**Ship**: "There's also another way to repeat a set of instructions, using a `for` loop. It's a more concise way to repeat a set of instructions."

**Tabitha**: "Concise, how so?"

**Ship**: "You don't need to keep track of an index variable and increment it, the `for` loop does that for you. Let's look at a scenario next."

Imagine now you're in the hydroponics bay and your program is running as part of an alien-trapping mechanism. You have a set of instructions that you need to repeat until the alien is caught.

```python
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
```

How it works:

- `for action in actions:` iterates over each action in the `actions` list.
- `random.choice([True, False])` simulates a random outcome for each action. A `True` means the action managed to catch the alien.
- `break` stops the loop when the alien is caught.
- `if not alien_caught:` checks if the alien was caught. If not, a message is displayed.
- The loop continues until the alien is caught or all actions are executed.

## `range()` in detail, control start, end and incrementation

**Ship**: "There's also the `range` construct..

**Tabitha** "Don't we need to get started with capturing the Alien, what if it gets away?"

**Ship**: "Yes, let's conclude this first. As I was saying, the `range` construct is a powerful way to control the iteration of a loop. You can control the start, end and incrementation of the loop. Let's look at an example."

```python
# Using range to simulate alien search attempts
for attempt in range(1, 11):  # Start at 1, end at 10
    print(f"Attempt {attempt}: Searching for the alien...")
    if attempt == 7:  # Simulate finding the alien on the 7th attempt
        print("Alien caught!")
        break
    else:
        print("Alien not found, trying again...")

# Output:
# Attempt 1: Searching for the alien...
# Alien not found, trying again...
# ...
# Attempt 7: Searching for the alien...
# Alien caught!
```

How it works:

- `for attempt in range(1, 11):` iterates over the range of numbers from 1 to 10.
- `if attempt == 7:` simulates catching the alien on the 7th attempt.
- The loop continues until the alien is caught or all attempts are made.
- The `range` construct allows you to control the start, end and incrementation of the loop.  

**Tabitha**: "So we've seen `while`, `loop` and now `range`, and I should use `range` when I need to control the start, end and incrementation of the loop, and use `while` when I need to repeat a set of instructions until a condition is met, and just `for` when I need to repeat a set of instructions a number of times. Got it, I think"

## Use `enumerate()` to get index and value

**Ship**: You've just seen how range can be used to get the index of a value. However, sometimes you need both the index and the value. With `range()` you can get the value but it's an extra line of code like so:

**Tabitha**: "Ok, but give me a scenario where this makes sense?"

**Ship**: "Imagine you have the alien, you're trying to catch it, and you have a list of actions you need to take to catch it. If you need to know which action you're on and what the action is then you need both the index and the value.

**Tabitha**: "Ok, sounds like I would use this if I want a lot of control over the loop."

**Ship**: Using `enumerate()` you can get both the index and the value like so:

```python
instructions = [
    "Set up trap",
    "Lure alien with food",
    "Activate motion sensors",
    "Close containment door"
]

alien_caught = False

for attempts, current_instruction in enumerate(instructions, start=1):
    print(f"Attempt {attempts}: Executing '{current_instruction}'...")
    # Simulate success on the 3rd instruction
    if attempts == 3:
        print(f"Success! Alien caught using: '{current_instruction}'")
        alien_caught = True
        break
    else:
        print(f"'{current_instruction}' failed. Moving to the next step...")

if not alien_caught:
    print("The alien escaped! We'll need a better plan next time.")
```

How it works:

- `for attempts, current_instruction in enumerate(instructions, start=1):` iterates over the `instructions` list, providing both the index and value.
- `if attempts == 3:` simulates catching the alien on the 3rd instruction.
- The loop continues until the alien is caught or all instructions are executed.
- The `enumerate()` function allows you to get both the index and value of an item in a list.
- The `start=1` parameter specifies the starting index of the enumeration.
- The `enumerate()` function is useful when you need both the index and value of an item in a list.

## Combining Data Sources in the Alien-Catching Scenario

**Ship**: In the context of catching an alien aboard a spaceship, you might have multiple data sources that can be combined to make your search more efficient. For example:

- **Sensor Data and Room Locations**  
    Combine data from motion sensors with a list of room locations to determine where the alien might be hiding.

    ```python
    sensors = ["Motion Sensor A", "Motion Sensor B", "Motion Sensor C"]
    rooms = ["Engine Room", "Hydroponics Bay", "Control Room"]
    sensor_readings = zip(sensors, rooms)

    for sensor, room in sensor_readings:
         print(f"{sensor} detected activity in the {room}.")
    ```

    Output:

    ```text
    Motion Sensor A detected activity in the Engine Room.
    Motion Sensor B detected activity in the Hydroponics Bay.
    Motion Sensor C detected activity in the Control Room.
    ```

- **Alien Behavior Patterns and Countermeasures**  
    Combine a list of observed alien behaviors with corresponding countermeasures to decide on the best course of action.

    ```python
    behaviors = ["Tampering with wiring", "Hiding in vents", "Avoiding light"]
    countermeasures = ["Seal wiring panels", "Deploy vent traps", "Activate floodlights"]
    strategies = zip(behaviors, countermeasures)

    for behavior, countermeasure in strategies:
         print(f"Behavior: {behavior} -> Countermeasure: {countermeasure}")
    ```

    Output:

    ```text
    Behavior: Tampering with wiring -> Countermeasure: Seal wiring panels
    Behavior: Hiding in vents -> Countermeasure: Deploy vent traps
    Behavior: Avoiding light -> Countermeasure: Activate floodlights
    ```

- **Crew Members and Assigned Tasks**  
    Combine a list of crew members with their assigned tasks to coordinate the search effort.

    ```python
    crew_members = ["Tabitha", "Dr. Singh", "Captain Reynolds"]
    tasks = ["Monitor sensors", "Prepare containment unit", "Coordinate search teams"]
    assignments = zip(crew_members, tasks)

    for member, task in assignments:
         print(f"{member} is assigned to: {task}")
    ```

    Output:

    ```text
    Tabitha is assigned to: Monitor sensors
    Dr. Singh is assigned to: Prepare containment unit
    Captain Reynolds is assigned to: Coordinate search teams
    ```

**Tabitha**: I see, it seems useful to combine data sources like alien behavior patterns and countermeasures to decide on the best course of action.

## list comprehension

**Ship**: "A list comprehension is a way to create a new list from an existing list. It's a very powerful construct and you'll see it used a lot in Python code. Let's look at an example in the context of catching the alien aboard our spaceship."

```python
# Define a list of alien sightings with their confidence levels
```python
alien_sightings = [
    {"location": "Engine Room", "confidence": 90},
    {"location": "Hydroponics Bay", "confidence": 75},
    {"location": "Control Room", "confidence": 50}
]


high_confidence_sightings = [
    sighting for sighting in alien_sightings if sighting["confidence"] > 70
]

print("High confidence sightings:")
for sighting in high_confidence_sightings:
    print(f"Location: {sighting['location']}, Confidence: {sighting['confidence']}%")
```

Here's how it works:

- `high_confidence_sightings = [sighting for sighting in alien_sightings if sighting["confidence"] > 70]` creates a new list of sightings with a confidence level greater than 70% using a list comprehension.
- The `if sighting["confidence"] > 70` condition filters the list of sightings based on the confidence level.
- The `for sighting in high_confidence_sightings:` loop iterates over the filtered list to display the high confidence sightings.  

**Ship**: "In this example, we filtered the list of alien sightings to only include those with a confidence level greater than 70%. This allows us to focus on the most likely locations where the alien might be hiding."

**Tabitha**: Looks like we should be looking in the Engine Room first!

**Ship**: "Exactly, well, to be on the safe side, let's check both the Engine Room and the Hydroponics Bay."

> [!NOTE]
> What we're seeing is a new list being created from an existing list. The new list is created using the following syntax:
>
> ```python
> [<expression> for <item> in <list> if <condition>]
> ```

> [!NOTE]
> **Fun Fact About Aliens**  
> Did you know that the Search for Extraterrestrial Intelligence (SETI) project has been scanning the skies for alien signals since the 1960s? Using powerful radio telescopes, SETI scientists analyze electromagnetic signals from space, hoping to detect patterns that might indicate intelligent life. One of the most famous events in SETI history is the "Wow! Signal," a strong, unexplained radio signal detected in 1977. Although it lasted only 72 seconds and has never been observed again, it remains one of the most intriguing mysteries in the search for extraterrestrial life!

## Assignment: Build an Alien Trap Simulation

In this assignment, you'll create a Python program that simulates an alien trap. The trap will use loops, conditionals, and user input to interact with the user and simulate capturing an alien. Here's the breakdown of the task:

### Requirements

1. **Setup the Trap**:
   - Use a `while` loop to simulate setting up the trap. The user must input the correct sequence of actions (e.g., "activate sensors", "arm lasers", "deploy net") to successfully set up the trap.
   - If the user inputs an incorrect action, prompt them to try again.

2. **Detect the Alien**:
   - Simulate alien detection using a `for` loop that iterates over a list of signals (e.g., ["weak signal", "no signal", "strong signal"]).
   - When a "strong signal" is detected, print a message indicating the alien is nearby.

3. **Capture the Alien**:
   - Use a `while` loop to simulate the capture process. The user must input commands (e.g., "close net", "activate containment field") to successfully capture the alien.
   - If the user inputs the wrong command, display a warning and allow them to try again.

4. **Escape Scenario**:
   - Add a random chance (using the `random` module) for the alien to escape during the capture process. If the alien escapes, restart the simulation.

5. **Victory Condition**:
   - Once the alien is successfully captured, display a congratulatory message and end the program.

### Example Output

```plaintext
Welcome to the Alien Trap Simulator!

Step 1: Set up the trap.
Enter the next action: activate sensors
Enter the next action: arm lasers
Enter the next action: deploy net
Trap successfully set up!

Step 2: Detect the alien.
Scanning signals...
Weak signal detected...
No signal detected...
Strong signal detected! Alien is nearby!

Step 3: Capture the alien.
Enter the next command: close net
Enter the next command: activate containment field
Alien captured successfully! Congratulations!
```

## Solution

[Solution](./solutions/solution.py)

## Quiz

**Question**: What is the output of the following spaceship navigation code?

```python
for i in range(3):
    print(f"Navigating to sector {i}")
```

**Question**: Why would I use a list comprehension over a for-loop in a spaceship's control system?

**Question**: What do `break` and `continue` do in a spaceship's loop control system?

[Solution quiz](./solutions/solution-quiz.md)