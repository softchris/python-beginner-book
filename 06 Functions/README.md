# Functions in Python

Functions are a fundamental building block of almost any programming language. It is a block of organized and reusable code that performs single or multiple actions. Additionally, functions provide better modularity for your code.

In this chapter, we will discuss the usage and dynamics of functions in Python.

In simple words, a function is like a mini-program within your program that does a specific job. You give it a name, and then you can "call" it by its name whenever you want it to carry out its job.

## Introduction

In this chapter, we will:

- Describe what Python functions are and their use.
- Define and call Python functions.
- Create and use parameters, arguments, and return values in Python functions.
- Apply knowledge of functions to solve complex problems.

## Narrative: Oxygen Failure

_The air smells off, and the oxygen system is failing. Tabitha must cleverly improvise using a toolkit and a bit of creativity to restore breathable air before passing out._

<div>
    <img src="./assets/oxygen-failure.jpeg" alt="Oxygen failure" width="600">
</div>

## Using functions

**Ship**: "Tabitha, the oxygen system is failing. You need to restore breathable air and we need to be quick about it"

**Tabitha**: "What? Ok, stay calm, I can do this. I'll use the toolkit to fix the oxygen system. What else can I use?"

**Ship**: "We need to address some faulty software, but in doing so we need to learn about functions"

**Tabitha**: "Ok, give me the short version, clock is ticking"

**Ship**: "First, you define a function that looks like this:""

```python
def regulate_oxygen():
    print("Oxygen levels are now stable.")

regulate_oxygen()
```

Let's explain the preceding code: 

- It defines a function `regulate_oxygen` using the `def` keyword.
- The function body is the `print` statement that prints "Oxygen levels are now stable."
- You call the function `regulate_oxygen` by writing `regulate_oxygen()`.

**Tabitha**: "Sounds good, but it's not that easy right?"

**Ship**: "Correct, we're encountering some issues calling a function with parameters. Let's dive deeper into functions."

## Functions with parameters

**Ship**: "Often, functions take parameters, values that you pass to the function when you call it. Let's look at an example."

```python
def regulate_oxygen(level):
    print("Oxygen levels are now stable at", level)

regulate_oxygen(21)
```

**Tabitha**: "I see, the function `regulate_oxygen` now takes a parameter `level`. When I call the function, I pass the value 21 to it. This is the value that the function uses when it prints the message."

**Ship**: "Correct, the value passed is called an argument. You can pass any number of arguments to a function as long as it maches the function definition. Here's another example with two arguments."

```python
def regulate_oxygen(level, location):
    print("Oxygen levels are now stable at", level, "in", location)

regulate_oxygen(21, "the control room")
```

**Tabitha**: "That looks useful, if we got an issue in the control room, we can address it directly.

**Ship**: "Exactly, there's another aspect of this, return values. Let's discuss that next."

## Returning values

**Ship**: "Functions can also return values, for example when we want the function to give us a result. Here's an example."

```python
def find_room_with_surplus(rooms, asked_surplus):
    """
    This function determines which rooms have a safe surplus of oxygen to extract.
    Each room must have at least the asked_surplus percentage left after deduction.
    """
    safe_rooms = {}
    for room, surplus in rooms.items():
        if surplus - asked_surplus >= 5:
            safe_rooms[room] = surplus - asked_surplus
    return safe_rooms

# Example usage
rooms = {
    "Control Room": 10,
    "Engine Room": 4,
    "Storage Room": 12,
    "Living Quarters": 16
}

asked_surplus = 3
safe_rooms = find_room_with_surplus(rooms, asked_surplus)
if safe_rooms:
    for room, remaining_surplus in safe_rooms.items():
        print(f"We can safely extract {asked_surplus}% oxygen from the {room}. Remaining surplus: {remaining_surplus}%.")
else:
    print("No room has a safe surplus of oxygen to extract.")
```

The preceding code works in the following way:

- The function `find_room_with_surplus` takes two arguments, `rooms` and `asked_surplus`.
- It returns a dictionary of rooms that have a safe surplus of oxygen to extract.
- The function is called with the `rooms` dictionary and the `asked_surplus` value.
- The result is stored in the `safe_rooms` variable and then printed out.

Running the code lets to an output like so:

```text
We can safely extract 3% oxygen from the Control Room. Remaining surplus: 7%.
We can safely extract 3% oxygen from the Storage Room. Remaining surplus: 9%.
We can safely extract 3% oxygen from the Living Quarters. Remaining surplus: 13%.
```

> [!TIP]
> Change the `asked_surplus` value to see how the output changes.
> Run this code from [Surplus code](./code/surplus.py)

**Tabitha**: "This is great, I can see how this will help, time to get to work right?"

**Ship**: "Almost, there's one more thing to discuss, chaining calls."

## Chaining calls

**Ship**: So far, you've seen how we call a function, with or without arguments and then do something with the result like printing it out. However, we can do more with it. 

We could also call a function and then use the return value from that function and pass it in as argument to another function. This way of calling functions is known as "chaining". Let's see an example:

```python
def calculate_oxygen_needed(people):
    # This function calculates the oxygen needed based on the number of people
    return people * 5  # Assume each person needs 5 units of oxygen

def adjust_oxygen_supply(oxygen_needed):
    # This function adjusts the oxygen supply by doubling the calculated need
    return oxygen_needed * 2

# Example usage in the spaceship scenario
crew_count = 10  # Number of crew members onboard
oxygen_required = calculate_oxygen_needed(crew_count)
adjusted_supply = adjust_oxygen_supply(oxygen_required)

print(adjusted_supply)  # The output will be 100
```

In the above example, we defined two functions to manage oxygen levels on the spaceship. Here's how they work together:

1. The `calculate_oxygen_needed` function determines the oxygen required based on the number of crew members.
2. The `adjust_oxygen_supply` function doubles the calculated oxygen to ensure a safe buffer.
3. The functions are called in sequence, or "chained," to calculate and adjust the oxygen supply.

This approach ensures that the spaceship maintains a safe and sufficient oxygen supply for all crew members.

**Tabitha**: "Great, makes sense, call one function, use the result in another. You know tick tock, we need to get this oxygen issue sorted."

## Built-in functions

**Ship**: "One last topic, lets not reinvent the wheel, there are built-in functions in Python that you can use. These functions are always available without defining them in the program."

Some examples of built-in functions are:

- `sum()`, sums all the elements in a list. Here's how you can use it:

    ```python
    list_A = [1,2,3,4]
    sum(list_A) # 10
    ```

- `len()`, counts the number of elements in a list. Here's how you can use it:

    ```python
    list_A = [1,2,3,4]
    len(list_A) # 4
    ```

- `type()`, describes the type of data. Here's how you can use it:

    ```python
    print(type(1)) # <class 'int'>
    print(type("a string")) # <class 'str'>
    print(type(True)) # <class 'bool'>
    print(print) # <built-in function print>
    ```

- `list()`, creates a list from an iterable. Here's how you can use it:

    ```python
    set_A = {1,2,3,4}
    list_A = list(set_A) # [1,2,3,4]
    ```

    List takes many types of iterables, like sets, tuples, strings, etc. and converts them into a list, so there's a lot of flexibility in how you can use it.

- `print()`, prints the value passed to it. Here's how you can use it:

    ```python
    print("Hello, World!") # Hello, World!
    ```

- `max()`, identifes and returns the maximum value in a list. Here's how you can use it:

    ```python
    list_A = [1,2,3,4]
    max(list_A) # 4
    ```

## Assignment

In this assignment, you will implement functions to regulate oxygen levels in a spaceship. The goal is to ensure that the oxygen levels are stable and safe for the crew. Here are some functions you might need to implement:

1. `regulate_oxygen(level, room)`: This function takes the oxygen level and the room name as arguments and prints a message indicating that the oxygen levels are stable.
1. `calculate_oxygen_needed(people)`: This function takes the number of people as an argument and returns the amount of oxygen needed for them.
1. `adjust_oxygen_supply(oxygen_needed)`: This function takes the amount of oxygen needed and returns the adjusted supply.
1. `find_eligible_rooms(rooms, asked_surplus)`: This function takes a dictionary of rooms and their oxygen surplus and the amount of surplus asked for. It returns a dictionary of rooms that have a safe surplus of oxygen to extract.

The general idea is that there are different rooms on the spaceship, each with a certain amount of oxygen surplus. By taking from the rooms with the most surplus, you can then distribute the oxygen to the rooms that need it most. 

An output from the program could look like this:

```text
Oxygen levels are now stable at 10% in the Control Room.
Oxygen levels are now stable at 10% in the Storage Room.
Oxygen levels are now stable at 10% in the Living Quarters.
No room has a safe surplus of oxygen to extract.
Adjusted oxygen supply needed: 100 units.
```

> TIP: start by defining the rooms and how much surplus they each have. Then you can define the functions to calculate the oxygen needed and adjust the supply. Finally, you can call the functions in sequence to get the desired output.

## Solution

[Solution](./solution.py)

## Quiz

**Question**. How do you define a function in Python?

1. Using the `function` keyword.

2. Using the `def` keyword.

3. Using the `func` keyword.

4. Using the `method` keyword

**Question**. What will be the output of the following code?

    ```python
    def add_numbers(x, y):
        return x + y

    result = add_numbers("3", "5")
    print(result)
    ```

1. 8

2. 15

3. "35"

4. Error

**Question**. Can you write a function without the `return` keyword?

1. Yes

2. No

[Solution quiz](./solutions/solution-quiz.md)

## Summary

In this chapter, you learned about creating functions as a way to organize and reuse code. You learned how to define functions, pass arguments, and return values. Additionally, you learned about chaining function calls and using built-in functions. Functions are a powerful tool in Python that can help you solve complex problems and make your code more modular and readable.
