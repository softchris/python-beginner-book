# Collection types

In Python, a collection is a group of objects. Python has several built-in collection types, including lists, sets, and dictionaries. These types are used to store multiple items in a single variable. The reason to use them is to hold multiple values in a single variable, which makes it easier to work with large amounts of data.

## Narrative: Ghost Ship

_Tabitha intercepts a distress signal from a derelict arkship. She needs to find out more why it looks abandoned. What happened to it?_

<div>
    <img src="./assets/arkship.jpeg" width="600" alt="Arkship plus smaller vessel">
</div>

## List, for storing multiple items in a single variable

**Ship**: "Tabitha, I'm spotting an object in my deep-space sensors. From what I can tell of the readings, it looks like an arkship. It's not responding to any hails. I'm sending you the coordinates."

**Tabitha**: "From what I know of our arkships they shouldn't be out here, right?"

**Ship**: "That's correct. All Arkships were sent out with different destinations, there shouldn't be any in this sector."

**Tabitha**: "There's a lot of readings you're sending me right now, I'm doing my best to store them all in a program like you taught me, see here at this program I wrote:

```python
reading_1 = "Hull integrity: 95%"
reading_2 = "Life signs: None detected"
reading_3 = "Power levels: Minimal"
reading_4 = "Radiation levels: Within safe limits"
reading_5 = "Spice residue: Trace amounts detected"

print("Readings from the arkship:")
print(reading_1)
print(reading_2)
print(reading_3)
print(reading_4)
print(reading_5)
```

**Ship**: "That's a good start, but I think we need to talk about lists as a better way to store multiple readings."

Lists are a collection type in Python that can store multiple items in a single variable. They are ordered, changeable, and allow duplicate values. 

You can create a list by placing the items inside square brackets `[]`, separated by commas. Here's how you can use a list to store the readings from the arkship:

```python
readings = [
    "Hull integrity: 95%",
    "Life signs: None detected",
    "Power levels: Minimal",
    "Radiation levels: Within safe limits",
    "Spice residue: Trace amounts detected"
]

print("Readings from the arkship:")
for reading in readings:
    print(reading)
```

**Tabitha**: "Oh, yea that looks a lot better. I'll use that from now on. I see a for loop being used also to go through the list. I'll remember that."

### Accessing elements in a list

**Ship**: "Yes, so organizing the data into a list is a good start, but you might also want to access individual elements in the list, for example to update or display them. Here's how you can access the hull integrity reading from the list:

```python
print("Hull integrity reading:", readings[0])

# Change the hull integrity reading
readings[0] = "Hull integrity: 90%"

# Display list item
last_reading = readings[len(readings) -1]
print("Last reading:", last_reading)
```

In the above code we:

- Access the first element of the list using `readings[0]`.
- Update the hull integrity reading to `90%`.
- Access the last element of the list using `readings[len(readings) - 1]`.

> [!NOTE]
> In Python, list indexes start at 0. So the first element of the list has an index of 0, the second element has an index of 1, and so on and the last element has an index of `len(list) - 1`. `len(list)` is a built-in helper function that returns the number of elements in the list.

## Dictionary, storing data in a more meaningful way

**Tabitha**: "I feel somehow that even if this is a step in the right direction, we only have one variable, it's hard to remember what index each reading is at. Is there a way to store the readings in a more meaningful way?"

**Ship**: "Yes there is, we can use a dictionary to store the readings. Dictionaries are another collection type in Python that store data in key value pairs. Each key is unique and maps to a value. Here's how you can use a dictionary to store the readings from the arkship:

```python
readings = {
    "hull_integrity": "95%",
    "life_signs": "None detected",
    "power_levels": "Minimal",
    "radiation_levels": "Within safe limits",
    "spice_residue": "Trace amounts detected"
}

print("Readings from the arkship:")
for key, value in readings.items():
    print(key + ":", value)

# add reading
readings["new_reading"] = "New reading value"
```

**Tabitha**: "That looks better I think, how do I access the hull integrity reading now?"

**Ship**: "You can access the value of a key in a dictionary using the key itself. Here's how you can access it via the key `hull_integrity`:

```python
print("Hull integrity reading:", readings["hull_integrity"])
```

**Tabitha**: "I see, that's a lot easier to remember. What if I don't know the name of the key, how do I access the readings then?"

### Accessing elements in a dictionary

**Ship**: "You can use `keys()` and `values()` methods to access the keys and values of a dictionary. This way, you don't need to know the key names in advance. Say you have access to a readings dictionary and want to investigate it further:

```python
print("Keys in the readings dictionary:")
for key in readings.keys():
    print(key)

print("Choose a key to display the value:")
chosen_key = input()
if chosen_key in readings:
    print(chosen_key + ":", readings[chosen_key])
else:
    print("Key not found")
```

**Ship**: "With the preceding code, you can safely access the values of the readings dictionary without knowing the key names in advance as we've built in some check using the `in` operator. If a key is not found, the code will print 'Key not found'. If the key is found, it will print the key and its value."

**Tabitha**: "I see, I like this, this means I can store the readings in a more meaningful way and access them easily and safely, so my program should look like this then:

```python
readings = {
    "hull_integrity": "95%",
    "life_signs": "None detected",
    "power_levels": "Minimal",
    "radiation_levels": "Within safe limits",
    "spice_residue": "Trace amounts detected"
}

print("Readings from the arkship:")
for key, value in readings.items():
    print(key + ":", value)

print("Choose a key to display the value:")
chosen_key = input()
if chosen_key in readings:
    print(chosen_key + ":", readings[chosen_key])
else:
    print("Key not found")
```

**Tabitha**: "I probably want to add additional functionalities like updating and adding more readings, but I think I can figure that out on my own now."

**Ship**: "Right, seems like the ship is undamaged so far based on the hull integrity reading. I'll try to bring us closer to the arkship for a closer look."

## Tuple, when you want to group related data

**Ship**: "Before we go closer, I wanted to mention another collection type in Python called a tuple. Tuples are similar to lists, but they are immutable, meaning you can't change the elements once they are assigned. 

A tuple has the following syntax:

```python
readings = ("Hull integrity", "95%")
```

In the preceding code, we're creating a tuple with two elements: the name of the reading and its value. Tuples are useful when you want to store related data that shouldn't change. It also provides a way to group data that's related, in this case the name of the reading and its value."

Here's how you can use a tuple to store the readings from the arkship:

```python
# Collect each reading as a tuple (name, value) and add it to a dictionary
readings_list = [
    ("Hull integrity", "95%"),
    ("Life signs", "None detected"),
    ("Power levels", "Minimal"),
    ("Radiation levels", "Within safe limits"),
    ("Spice residue", "Trace amounts detected")
]

# read each entry in the list
for reading in readings_list:
    print(reading[0] + ":", reading[1])
```

**Ship**: "What's interesting about the preceding code is that we're using a tuple to store each reading as a pair of values. That separates the name of the reading from the value, making it easier to read and understand the data." 

**Tabitha**: "How do I know wether to use a list, a tuple, or a dictionary?"

**Ship**: "That's a good question. Here's a general guideline:

- Use a list when you have a collection of items that need to be ordered and can change.
- A tuple is useful when you have a collection of items that should not change, also when you want to group related data together.
- Dictionary is for when you have a collection of items that need to be accessed by a key.

## Assignment

**Ship**: "I need you to take a small transporter ship and go to the arkship. I'll stay here and monitor the situation. I'll program the transporter to take you there." 

Task: Write a program that stores the readings from the arkship in a dictionary and allows the user to access the readings by entering the key. The program should have different commands like list, add, update and exit.

Here's what a run of the program could look like:

```text
Commands: list, add, update, exit
Enter command: add
Enter key: oxygen
Enter value: 90%
Commands: list, add, update, exit
Enter command: list
Readings from the arkship:
oxygen: 90%
Commands: list, add, update, exit
Enter command: add
Enter key: hull integrity
Enter value: 95%
Commands: list, add, update, exit
Enter command: list
Readings from the arkship:
oxygen: 90%
hull integrity: 95%
Commands: list, add, update, exit
Enter command:
```

## Solution

[Solution](./solutions/solution.py)

## Quiz

**Question**:
What is the main difference between a list and a tuple in Python?

1. A list is immutable, while a tuple is mutable.
2. A list is mutable, while a tuple is immutable.
3. A list can only store strings, while a tuple can store any data type.

**Question**:

How do you access the value of a key in a dictionary?

- By using the `get()` method only.
- By using the key itself, e.g., `dictionary[key]`.
- By iterating through the dictionary and checking each key.

[Solution quiz](/.solutions/solution-quiz.md)

## Summary

In this chapter, you learned about different collection types in Python: lists, sets, dictionaries, and tuples. You saw how that was a good way to store multiple values in a single variable.

Lists are good for storing ordered collections of items that can change, whereas dictionaries are useful for storing key-value pairs that can be accessed by a key. Tuples are similar to lists but are immutable, meaning they can't be changed once they are assigned. Additionally, Tuples are useful for storing related data that shouldn't change.
