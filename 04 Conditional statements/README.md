# Conditional Statements in Python

When you need to enable the code make decisions and execute different actions based on those decisions, we use conditional statements. Let's dive deeper into the concept of conditional statements in Python.

## Introduction

In this chapter, we will:

1. Understand what conditional statements are and their importance in Python.
2. Implement `if`, `elif`, and `else` statements in Python.
3. Construct complex conditions using logical operators.

## Narrative: Gravity Flip

*The artificial gravity is on the fritz! One moment you're floating like an astronaut, the next you're slammed back to the floor like a sack of potatoes. Tabitha, our quick-thinking hero, must fix the gravity controls while dodging flying objects and navigating a topsy-turvy world where nothing stays put. Can she restore order before chaos takes over?*

<div>
    <img src="./assets/gravity.jpeg" alt="Gravity flip" width="600">
</div>

## What are the types of conditional statements?

1. `if` statement: If x condition is true than execute the below code.
2. `else` statement: If the above `if` condition is not satisfied then execute the `else` statement block.
3. `elif` statement: Used in scenarios where you need to provide multiple `if` statements but only after the primary `if` statement.

## `if` Statement

**Ship**: "Tabitha, my system is malfunctioning! I can't control the gravity. You need to fix it."

**Tabitha**: "You don't say, I'm up here in the ceiling. Ok walk me through it, what do I need to do?"

**Ship**: "There are some controls that need switching, and the system indicates there seems to be a faulty control. Lots of logic in that control. We need to talk about if-statements".

The `if` statement is very straightforward. It checks whether a condition is `True`. The code inside the `if` block is only executed if the condition is `True`.

The structure of the `if` statement block is quite simple. You start with an `if` keyword followed by the condition. Then a colon `:` to start the code block that needs to be executed if the condition is `True`.

```python
```python
gravity_level = 5

print("Current gravity level is", gravity_level)
if gravity_level > 3:
    print("Gravity is above safe levels!")
    print("Is gravity level greater than 3? Answer - ", gravity_level > 3)

if gravity_level < 10:
    print("Gravity is within operational limits.")
    print("Is gravity level greater than 10? Answer - ", gravity_level > 10)

# The below if statement will execute but the code block will not be executed
# Why? - Because gravity level is 5 and 5 is not greater than 10.

if gravity_level > 10:
    print("This will never be printed")
    
# The condition gravity_level > 10 results in FALSE. And if the result of a condition is FALSE...
# ...it will never execute the code block
```

Output:

```text
Current gravity level is 5
Gravity is above safe levels!
```

**Tabitha**: "I feel there's some logic missing here, gravitation is clearly not too high but too low."

**Ship**: "Yes, you are right. We need to add an `else` statement to handle the scenario when the condition is `False`."

## `else` Statement

An `else` will always be followed by an `if` statement. `else` statements are ONLY executed when the `if` statement’s condition is `False`.

```python

gravity_level = 5
print("Current gravity level is", gravity_level)

if gravity_level > 10:
    print("Gravity is dangerously high!")  # This will not be executed, as the condition is False
else:
    print("Gravity is within safe limits.")  # This will be executed, because the if condition is False
```

Output:

```text
Current gravity level is 5
Gravity is within safe limits.
```

**Tabitha**: "Better, but there's still no logic indicating that gravity is too low - like now ! Let me guess, there's another construct for that?"

**Ship**: "Yes, I was getting to that. We need to add an `elif` statement to handle the scenario when the condition is not satisfied by the `if` statement."

> [!NOTE]  
> **Fun Fact:** Did you know that gravity is not the same everywhere on Earth? The force of gravity is slightly weaker at the equator compared to the poles due to the Earth's rotation and its slightly flattened shape!  
>
> Gravity also varies significantly across the solar system. For instance, the Sun's gravity is about 28 times stronger than Earth's, which is why it holds all the planets in orbit. On Jupiter, the largest planet in our solar system, gravity is about 2.4 times stronger than Earth's, making it a challenge for any spacecraft to escape its pull. Conversely, on the Moon, gravity is only about 1/6th of Earth's, which is why astronauts could hop and leap so easily during the Apollo missions.  
>
> Understanding gravity on different celestial bodies is crucial for space exploration and designing missions that can safely land and return to Earth.

## `elif` Statement

The logic of `elif` comes from the combination of `else` and `if`. `elif` comes right after `if` statement. When the condition of `if` statement is false, the `elif` is executed.

> Note: `elif` needs an `if` statement prior to it, but doesn't require an `else` statement after it.

```python
gravity_level = 5

if gravity_level > 10:
    print("Gravity is dangerously high! Immediate action required.")
elif gravity_level > 3:
    print("Gravity is at operational levels but needs monitoring.")
else:
    print("Gravity is too low! Adjustments are necessary to stabilize the environment.")
```

Output:

```text
Gravity is at operational levels but needs monitoring.
```

**Tabitha**: "I can tell you right now, gravity is too low, it's not a 5"

**Ship**: "Well, then we need a new reading"

## Assignment

**Ship**: "Your mission is to adjust the program so that it prints the correct message based on the gravity level. I found this routine you can use for that:"

```python
def read_gravity():
    level = int(input("Enter the gravity level: "))
    return level
```

**Ship**: "Call it by typing like so `gravity_level = read_gravity()`."

Combine all the code you have so far. I can do the rest from there to integrate it into the system.

## Solution

[Solution](./solutions/solution.py)

## Quiz

**Question**. In a Python conditional statement, what will happen if the condition in the `if` statement is `False` and no else or `elif` statement follows it?

1. An error will occur

2. The program will stop

3. Nothing will happen and the program will continue

4. The condition will be checked again

**Question**. How many `elif` statements can you have in a Python conditional block?

1. Only one

2. Only two

3. As many as you want

4. None

**Question**. Consider the following Python code snippet:

```python
x = 10
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")
```

What will be the output?

1. x is greater than 10

2. x is equal to 10

3. x is less than 10

4. The code will give an error

[Solution quiz](./solutions/solution-quiz.md)

