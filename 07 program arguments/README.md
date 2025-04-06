
# Program arguments

Program arguments is a way to pass data into a program when you run it. This is a common way to control the program and carry out differing actions depending on what input is passed. This especially useful when you want to run the same program with different input data.

It's used in many different types of programs, from simple scripts to complex applications, for example a program that searches the logs of a machine and you want to pass a date interval, but also in backup scripts, data processing scripts and so on.

## Narrative: Drones gone rogue

*A group of cleaning drones have gone rogue, whizzing through the corridors at high speed and causing chaos. Tabitha redirects them into a storage bay after an exhilarating chase.*

<div>
  <img src="./assets/cleaning.jpeg" width="600" alt="Cleaning gone rogue">
</div>

## Introduction

In this chapter, we will:

- Learn how to run Python code from a file.
- Pass data into a program when you run it.
- Make a program that searches the logs of a machine.

## Run Python code from a file

**Ship**: "Tabitha, we've got a problem. The cleaning drones have gone rogue and are causing chaos in the corridors. Can you help us?"

**Tabitha**: "Tell me about it, they just cleaned me into a corner, I'm stuck in the storage bay. What do I need to do?"

**Ship**: You should have access to a terminal where you are. You need to diagnose the problem and find a way to stop them.  

**Tabitha**: "Ok, on it! What am I looking for?"

**Ship**: "There should be a cleaning log on the ship's computer. You need to search the logs for the last 24 hours and find out what's been going on. I should probably tell you how program arguments work."

So far, you've seen how you can run Python code via its REPL but perhaps the more common way is to place said code in a file and use the Python executable to run it. What you need is to create a text with the file ending `.py` and place Python code in it like below code:

```python
# cleaning.py

import schedule
import time

def clean():
  print("Cleaning in progress...")

# Schedule cleaning at common intervals
schedule.every(1).hour.do(clean)
schedule.every().day.at("12:00").do(clean)
schedule.every().monday.do(clean)

print("Cleaning schedule initialized. Waiting for the next task...")

while True:
  schedule.run_pending()
  time.sleep(1)
```

In the preceding code, we have a simple program that schedules cleaning at common intervals.

- The `schedule` module is used to schedule tasks at specific intervals.
- The `time` module is used to sleep the program for a second.
- The `clean()` function is called when it's time to clean, this is setup with the code `schedule.every(1).hour.do(clean)`.
- - It will run its action every hour, every day at 12:00 and every Monday as instructed by the code `schedule.every(1).hour.do(clean)`, `schedule.every().day.at("12:00").do(clean)` and `schedule.every().monday.do(clean)`.
- The program then runs in a loop, checking if it's time to clean and then sleeps for a second, this is done with the code `schedule.run_pending()` and `time.sleep(1)`. 

To run the preceding code you type the following in a terminal:

```bash
python cleaning.py
```

You should see an output that says:

```text
"Cleaning schedule initialized. Waiting for the next task...
```

Once it matches the setup time, you should see the output "Cleaning in progress...".

**Tabitha**: "I see, so I can run Python code from a file by using the Python executable and the file name. You asked me to fix the cleaning drones, right, so do I find a program like the above and fix the code then?"

**Ship**: "Yes, but there are different ways to fix the problem. You can either change the source code or change the data that is passed into it. The latter is done by using program arguments. We don't know yet what the problem is so we need to investigate first."

## Passing arguments

**Ship**: Not only can you run Python code via a file, you can also provide data input to the execution, like so for example:

```python
python cleaning.py 14:00
```

**Tabitha**: "Ok, but does that do?"

**Ship**: "In the program we say, that does nothing, but let's change that. Let's do first things, first, learn how we capture the input data, secondly, let's change the program to use this input data."

### Reading arguments

**Ship**: "To read this input data you need the `sys` module and the arguments can be found at `sys.argv`."

```python
# example.py

import sys

# store args in a variable list
args = sys.argv
print(args) # ["example.py"] if called with python example.py
```

In the preceding code, you see how `sys.argv` is used to read the input data. Given that you call this program with `python cleaning.py`, i.e providing no input arguments, you get the response `[".\\cleaning.py"]` an array with one item, the program name.

### Use the arguments

**Ship**: "Let's change the program to use this input data."

```python
# cleaning.py

import sys
import schedule
import time

def clean():
  print("Cleaning in progress...")


args = sys.argv
time_to_clean = args[1]

# Schedule cleaning at common intervals
schedule.every(1).hour.do(clean)
schedule.every().day.at(time_to_clean).do(clean)
schedule.every().monday.do(clean)

print("Cleaning schedule initialized. Waiting for the next task...")


while True:
  schedule.run_pending()
  time.sleep(1)
```

In the preceding code we:

- Read the input data from `sys.argv` and store it in a variable `args`.
- We then access the first argument in the list `args[1]` and store it in a variable `time_to_clean`.
- We then use this variable in the code `schedule.every().day.at(time_to_clean).do(clean)` to schedule the cleaning at the time provided.

**Tabitha**: "I see, so I can pass data into a program when I run it. But what happens if I don't provide the correct number of arguments?"

**Ship**: "Good catch, you should always check that you have the correct number of arguments and if it's missing, you need to decide whether to print an error message or use a default value."

**Tabitha**: "Ok, can you show me how we update the code to handle this?"

**Ship**: "Sure, let's do that."

### Handling missing arguments

**Ship**: "Let's change the program to handle missing arguments."

```python
# cleaning.py

import sys
import schedule
import time

def clean():
  print("Cleaning in progress...")

args = sys.argv

if len(args) < 2:
  print("Please provide the time to clean")
else:
  time_to_clean = args[1]

  # Schedule cleaning at common intervals
  schedule.every(1).hour.do(clean)
  schedule.every().day.at(time_to_clean).do(clean)
  schedule.every().monday.do(clean)

  print("Cleaning schedule initialized. Waiting for the next task...")

  while True:
    schedule.run_pending()
    time.sleep(1)
```

In the preceding code, the program will print an error message if the correct number of arguments is not provided.

**Tabitha**: "I see, but what if we rely on a default value if the argument is missing?"

**Ship**: "You can do that too, let me show you how."

### Using default values

**Ship**: "Let's change the program to use a default value if the argument is missing."

```python
# cleaning.py

import sys
import schedule
import time

def clean():
  print("Cleaning in progress...")

args = sys.argv

if len(args) < 2:
  time_to_clean = "12:00"
else:
  time_to_clean = args[1]

# Schedule cleaning at common intervals
schedule.every(1).hour.do(clean)
schedule.every().day.at(time_to_clean).do(clean)
schedule.every().monday.do(clean)

print("Cleaning schedule initialized. Waiting for the next task...")
```

**Ship**: "Now that you have learned how to pass data into a program, can you locate the cleaning log and search for the last 24 hours? For some reason, I don't have access to the logs in the storage bay."

**Tabitha**: "Sure, I assume I'm looking for a file called `cleaning.log` something, give me a moment"

## Assignment

**Tabitha**: "I found something I think, here's a bunch of logs, let me see if I can find something interesting."

```text
2023-01-01 12:00:00 INFO Cleaning in progress at Corridor A...
2023-01-01 12:00:05 INFO Cleaning in progress at Storage Bay...
2023-01-01 12:00:10 INFO Cleaning in progress at Engine Room...
2023-01-01 12:00:15 INFO Cleaning in progress at Control Room...
2023-01-01 12:00:20 INFO Cleaning in progress at Corridor B...
2023-01-01 12:00:25 INFO Cleaning in progress at Hangar...
...
```

**Tabitha**: "This doesn't look right, cleaning every 5 seconds, I know there's more than one drone but this is too often. Let's see if I can find the program that it runs. There you are `cleaning-ship.py`, let's see what you do."

```python
# cleaning-ship.py

import sys
import schedule
import time

def clean(location):
  print(f"Cleaning in progress at {location}...")

args = sys.argv

if len(args) < 2:
  location = "Default Location"
else:
  location = args[1]

# Schedule cleaning at common intervals
# Ha, should be fun!
schedule.every(5).seconds.do(clean, location=location)

print("Cleaning schedule initialized. Waiting for the next task...")
```

**Tabitha**: "I think I spot the problem, someone had fun with the cleaning schedule."

```python
# Ha, should be fun!
schedule.every(5).seconds.do(clean, location=location)
```

**Tabitha**: "Let me write a fix, it should be every hour, like so."

Task: Write the fix for the cleaning schedule. Remember that both the location and the time to clean should be passed as arguments.

> [!NOTE]
> To run your solution, you need to call `pip install schedule` as it's not part of the standard library. Then you can call your program with `python <name of your file>.py "Corridor A" "12:00"`.

**Tabitha**: "I wonder who would type "ha" and change the code like that"

## Quiz

**Question**: **What is the purpose of `sys.argv` in Python?**

1. To schedule tasks at specific intervals.
2. To read input arguments passed to a Python program.
3. To print the current system time.

**Question**: **What happens if you don't provide the correct number of arguments to a program using `sys.argv`?**

1. The program will always use default values.
2. The program may throw an error or behave unexpectedly.
3. The program will automatically prompt the user for input.

[Solution quiz](./solutions/solution-quiz.md)

## Summary

In this chapter, you explored how to pass arguments to Python programs and use them effectively. You learned how to run Python code from a file and then moved on to capturing input data using the `sys.argv` list.

Then you moved on to to handle missing arguments by either displaying an error message or using default values.

Additionally, you examined how to modify a program to accept multiple arguments and use them in scheduling tasks.

Finally, through a narrative example, you identified and fixed a bug in a cleaning schedule program, showcasing the importance of program arguments in debugging and customization.
