# User input

There will be times when you want to interact with the user, either by asking for input or by providing output. Python has a few ways to do this, and in this chapter, we will explore some of them.

## Introduction

In this chapter we will:

- Use the `input()` function to collect user input.
- Make a function more reusable by adding parameters.
- Build a simple calculator.

## Narrative: Star chart scramble

_The navigation system goes offline, forcing Tabitha to manually align the ship by using the stars outside—a high-stakes task requiring precision and quick thinking._

<div>
    <img src="./assets/navigation-system.jpeg" width="600" alt="Navigation system">
</div>

## Why is user input important?

**Ship**: "Tabitha, we've got another problem unfortunately. The navigation system is down, and well, it needs your immediate attention.

**Tabitha**: "We're never getting there are we? What's the problem this time?"

**Ship**: "The navigation system is offline, and you need to manually align the ship by using the stars outside. It's a high-stakes task requiring precision and quick thinking."

**Tabitha**: "Tell, me more about the problem."

**Ship**: "So there are sensors all over the ship that can detect the stars outside. You need to input the star coordinates into the navigation system from all these sensors. The system will then calculate the ship's position and course. Therefore, you need to learn how to input data into the system."

User input is a critical aspect of programming because it allows your programs to interact dynamically with users. Instead of hardcoding values, you can make your programs more flexible and adaptable by accepting input during runtime. This is especially useful for applications like calculators, games, or any software that requires user interaction.

## Using `input()` function

**Ship**: "Tabitha, you can use the `input()` function to get input from the user. It waits for the user to type something and press Enter. See here in below example:

```python
# Collect sensor values manually and send to the ship's mainframe

import sys
from datetime import datetime

def send_to_mainframe(data, user, timestamp):
    # Simulate sending data to the ship's mainframe
    print(f"Sending data to mainframe: {data}")
    print(f"Recorded by: {user} at {timestamp}")

# Ask for the user's name
user_name = input("Enter your name: ").strip()

# Ask for sensor values
print("Enter sensor values (press Enter when done):")
sensor_data = input().strip()

# Get the current timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if sensor_data:
    send_to_mainframe(sensor_data, user_name, current_time)
else:
    print("No sensor data provided.")
```

In this example, we:

- Use the `input()` function to ask the user for their name and sensor values.
- Use the `datetime` module to get the current timestamp.
- Call the `send_to_mainframe()` function to simulate sending the sensor data to the ship's mainframe.
- Display a message if no sensor data is provided.
- Call `strip()` to remove any leading or trailing whitespaces from the input. 

**Tabitha**: "I see, so the `input()` function is used to get input from the user. This actually looks like code I could use for the star chart alignment task."

**Ship**: "Exactly, but there are some things you need to keep in mind when using the `input()` function. For example, it always returns a string, so you may need to convert it to a different type if you're expecting a number or other data type."

## Handling number input

**Ship**: "Some value you might want to collect from the user could be a number. In Python, you can convert a string to an integer using the `int()` function. Let's see how we can do this:

```python
import sys

# Prompt the user for input
user_input = input("Enter a number: ").strip()

# Convert the input to an integer
try:
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Error: Please enter a valid number.")
```

In this example, we:

- Use the `input()` function to ask the user for a number.
- Apply the `int()` function to convert the input to an integer.
- Enclose the conversion in a `try` block to catch any errors that may occur.
- Call `strip()` to remove any leading or trailing whitespaces from the input, in case you input a number with spaces.

**Tabitha**: "Ok, so for certain sensor values, I might need to convert them to numbers. This is good to know."

**Ship**: "Yes, and sometimes we're even dealing with decimal numbers. In that case, you can use the `float()` function to convert a string to a floating-point number."

In above code we:

- Ask the user for two inputs: the amount of fuel to transfer and the energy required for the hyper drive.
- Combine these inputs, and display the total power available for the mission.
- Convert the inputs to integers using `int()` to perform the calculation. 
- Catch the errors. If the user enters non-numeric values, we catch the `ValueError` and display an error message.  

Imagine you run this like so:

```bash
Enter the amount of fuel to transfer (in units): 11
Enter the energy required for the hyperdrive (in units): 2
Combining 11 units of fuel with 2 units of energy...
Total power available for the mission: 13 units
```

### Handling errors

Let's take our time a little with error handling and zoom in on error handling:

```python
import sys

# Prompt the user for input
user_input = input("Enter a number: ").strip()

# Convert the input to an integer
try:
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Error: Please enter a valid number.")
```

We write the code this way as we want to make sure it's robust enough to handle a user mistyping. If you type for example `hello` instead of a number, the program will catch the error and print an error message.

**Tabitha**: "Ok, nice, but the program quits anyway, can't we have it so the program keeps asking for input until the user provides a valid number?"

**Ship**: "Yes, of course, we just need to wrap it in a loop like so:"

```python
import sys

while True:
    # Prompt the user for input
    user_input = input("Enter a number: ").strip()

    # Convert the input to an integer
    try:
        number = int(user_input)
        print(f"You entered: {number}")
        break
    except ValueError:
        print("Error: Please enter a valid number.")
```

**Tabitha**: "So the above works then?"

**Ship**: "Yes, it will keep asking for input until the user provides a valid number."

**Tabitha**: "Great, anything else I should know?"

**Ship**: "Yes, sometimes you need to read multiple lines of input. Let's see how you can do that next."

## Multiline input

**Ship**: Use `sys.stdin.read()` to read multiple lines of input. Here's how:"

```python
import sys

print("Enter your input (press Ctrl+D or Ctrl+Z to finish):")
answer = sys.stdin.read().strip()

print(f"You entered: {answer}")
```

Here's what running the program could look like:

```bash
python multiline_input.py
hi
there
I'm Tabitha
^D
You entered: hi there I'm Tabitha
```

**Ship**: Let's take a realistic example Tabitha, you're collecting measurement values from the ship's sensors. You want to collect multiple values from the user and present them to the user. Here's how you could do it:

```python
# collect multiple values from sensors
import sys

print("Enter sensor values (press Ctrl+D or Ctrl+Z to finish):")

answer = sys.stdin.read().strip()

# do something with the values

print(f"Sensor values: {answer}")
```

**Tabitha**: "Ok, so then I could input 11 114 23 47 etc. and the program would collect all these values?"

**Ship**: "Exactly, you can input as many values as you want, and the program will collect them all."

## Assignment, fixing navigation system

**Ship**: "Time to fix the navigation system Tabitha. We need to collect values from multiple sensors, first sensor emits 1 whole number, the second sensor emit 1 decimal number and the third sensor emit 0 or 1 (we can interpret this as a boolean).  

Task: Write a program that collects these sensor values and sends them to the mainframe. The latter function `send_to_mainframe` is already implemented for you, you just need to call it"

Here's what a run of the program can look like:

```text
Enter your name: Tabitha
Enter a whole number: 1
Sending data to mainframe: {'sensor1': 1}
Recorded by: Tabitha at 2025-03-23 21:31:57
Enter a decimal number: 11.2
Sending data to mainframe: {'sensor2': 11.2}
Recorded by: Tabitha at 2025-03-23 21:32:02
Enter a boolean value (0 or 1): 1
Sending data to mainframe: {'sensor3': True}
Recorded by: Tabitha at 2025-03-23 21:32:09
```

## Solution

[Solution](./solutions/solution.py)

## Quiz

**Question:** In Python, how do you get input from a user and store it in a variable called `user_response`?

1. `user_response = input()`
2. `user_response = get.input()`
3. `user_response = user.input()`

[Solution quiz](./solutions/solution-quiz.md)
