# Operators in Python

In the real world, when you wish to perform arithmetic calculations between two or more numbers, you use symbols like `+`, `-`, `/`, etc. Similarly, operators in Python are special symbols that perform some computation designated to them.

## Introduction

In this chapter, we will:

- Understand the use of operators in Python
- Inspect the different types of operators in Python
- Leverage operators to perform arithmetic calculations between variables and integers.

## Narrative: Rerouting the Power Supply

*After some additional digging, Tabitha started to get a better grip of the overall ship's design. She could say she understood its major compartments but more importantly she got some displays working telling her about the power supply, where it worked, where it didn't. Ok, she thought, Engines have NO power, shields good, life support good, but working bay has tons of power for no good reason, what if I could divert some of that power to the engines?*

<div>
    <img src="./assets/Chapter3.jpeg" alt="Rerouting power supply" width="600">
</div>

## What are operators and operands?

**Tabitha**: Alright, Ship, let's figure this out. The engines need power, but I can't just reroute energy recklessly. If I take too much from the working bay, I risk damaging the engines or blowing a fuse. Let's calculate this carefully using Python.

**Ship**: Yes Tabitha, we've discussed data types, variables and even how to work with terminal inputs. Now, let's talk about operators.

Imagine this, you have five engines, and you are given three more. You quickly do 5 `+` 3, and now you have 8 engines. 

- The operation performed is called "addition".
- The symbol that performs the addition `+` is called the "operator".
- While the values `5` and `3` on which the addition operation was performed are called the "operands".

Consider the following example:

```python
working_bay_energy = 50
engine_min_value = 10
engine_max_value = 100
energy_rerouted = 30

print("The working bay initially had", working_bay_energy, "units of energy. Tabitha decided to reroute", energy_rerouted, "units of energy to the engines.")
print("After rerouting, the working bay is left with", working_bay_energy - energy_rerouted, "units of energy.")
print("Using the rerouting equation, the engine effect is calculated as:")
engine_effect = ((energy_rerouted + 3) * 5) / 4
print("Engine effect =", engine_effect)

if engine_min_value <= engine_effect <= engine_max_value:
    print("The engine effect is within the safe limits.")
else:
    print("Warning: The engine effect is outside the safe limits!")
```

This code will print the following:

```text
The working bay initially had 50 units of energy. Tabitha decided to reroute 30 units of energy to the engines.
After rerouting, the working bay is left with 20 units of energy.
Using the rerouting equation, the engine effect is calculated as:
Engine effect = 41.25
The engine effect is within the safe limits.
```

In the above example, we have carried out the operations addition, subtraction, multiplication, and division. 

To test the above example, you can type or paste the [code](./code/engine.py) in your editor and run it via the terminal like so:

- Navigate to *code/* folder.
- Run the command `python engine.py`

**Tabitha**: "That looks useful, Ship. I can see how operators can help me with this scenario"

### Categories of operators

**Ship**: "Let's talk more about operators. We can categorize operators into the following sub-categories:"

- **Arithmetic operators**, operators that allow you to add, subtract, multiply, and so on. For example, calculating the total distance traveled by a spaceship: `distance_in_light_years + additional_distance_in_parsecs * 3.26` (since 1 parsec ≈ 3.26 light-years).
- **Comparison operators**, operators that allow you to compare two values. For example, checking if the distance to a star is closer than another: `distance_to_star_in_light_years < distance_to_planet_in_light_years`.
- **Assignment operators**, operators that allow you to assign values to a variable. For example, assigning the distance to the nearest star: `distance_to_proxima_centauri = 4.24` (in light-years).

**Tabitha**: "I see, so operators are like tools that help me perform different operations. I can use them to calculate, compare, and assign values. Ok, what else?"

### Arithmetic operators

**Ship**: Let's dive into arithmetic operators. There are a few.


| Operator |      Name      |       Example       | Description                                                                                                                          |
|:--------:|:--------------:|:-------------------:|--------------------------------------------------------------------------------------------------------------------------------------|
| `+`        | Addition       | 5 `+` 3 is equal to 8   | The `+` operator is used for adding two values, like calculating the total distance traveled by a spaceship in light-years.            |
| `-`        | Subtraction    | 9 `-` 4 is equal to 5   | The `-` operator is used for subtracting one value from another, such as determining the remaining fuel after a journey.               |
| `*`        | Multiplication | 4 `*` 10 is equal to 40 | The `*` operator multiplies values, useful for calculating the energy output of multiple solar panels on a space station.              |
| `/`        | Division       | 8 `/` 2 is equal to 4   | The `/` operator divides the first value by the second, like splitting the power supply evenly between two spaceship modules.          |
| `//`       | Floor Division | 5 `//` 2 is equal to 2  | The `//` operator performs division but rounds down the result to the nearest whole number, such as determining how many full orbits a satellite completes in a given time. |
| `**`       | Power of       | 5 `**` 2 is equal to 25 | The `**` operator multiplies the first number to itself. The second number specifies how many times it should be multiplied, like calculating the gravitational force between celestial bodies. |
| `%`        | Modulus        | 5 `%` 2 is equal to 1   | The `%` operator returns the remainder of a division operation, useful for determining the leftover energy after distributing it among spaceship systems. |

**Tabitha**: Oh, I like this so much space :)

**Ship**: "Yes, glad you like it. Let's see some examples next."

Observe the example below:

```python
# Navigating Between Two Points in Space

start_point = "Jupiter"
end_point = "Interstellar Space"
obstacles = ["Asteroid Belt"]

print("The navigation system is tasked with plotting a course from", start_point, "to", end_point, "while avoiding obstacles like the", obstacles[0], ".")

# Calculate the distance between Jupiter and the edge of the solar system
distance_to_edge_of_solar_system = 1000  # in arbitrary space units
speed_of_ship = 250  # in space units per hour
time_to_travel = distance_to_edge_of_solar_system // speed_of_ship  # Floor division for whole hours
remaining_distance = distance_to_edge_of_solar_system % speed_of_ship  # Modulus for remaining distance

print("The distance to the edge of the solar system is", distance_to_edge_of_solar_system, "units.")
print("At a speed of", speed_of_ship, "units per hour, the journey will take approximately", time_to_travel, "hours with", remaining_distance, "units left to travel.")

# Navigating past the asteroid belt
safe_distance = 50  # minimum safe distance from the asteroid belt
current_distance_from_asteroid_belt = 60  # current distance from the asteroid belt

if current_distance_from_asteroid_belt >= safe_distance:
    print("The ship is maintaining a safe distance of", current_distance_from_asteroid_belt, "units from the asteroid belt.")
else:
    print("Warning: The ship is too close to the asteroid belt! Adjusting course...")

# Final navigation check
print("Navigation system confirms the course from", start_point, "to", end_point, "is clear and safe for travel.")
```

In the code above, we:

- Calculate the time it takes to travel from Jupiter to the edge of the solar system.
- Determine the remaining distance after the ship reaches the edge of the solar system.
- Check if the ship is maintaining a safe distance from the asteroid belt.
- Confirm the course from Jupiter to interstellar space is clear and safe for travel.
  
Note the use of the operators `//` and `%` for floor division and modulus operations, respectively.

**Tabitha**: "Taking notes, I need to know this stuff as a captain on the bridge"

**Ship**: "Well, this is just a simulation of what it can look like, but good that you take notes :)"

## Comparison operators

**Ship**: There's more operators you should know about, and you've seen some in use already, namely comparison operators.

Comparison operators in Python are used to compare two values. They return a `Boolean` value (`True` or `False`).
| Operator |        Name        |      Example     | Description                                                                                                                                                                                             |
|:--------:|:------------------:|:----------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<`        | Less than          | `fuel_level < 50` is `True`   | The `<` operator checks if the value of the left operand is less than the value of the right operand. For instance, checking if the fuel level is below 50 units: `fuel_level < 50` returns `True`.    |
| `>`        | Greater than       | `engine_temp > 100` is `True`   | The `>` operator checks if the value of the left operand is greater than the value of the right operand. For example, verifying if the engine temperature exceeds 100 degrees: `engine_temp > 100` returns `True`. |
| `<=`       | Less than equal    | `oxygen_level <= 75` is `True`   | The `<=` operator checks if the value of the left operand is less than or equal to the value of the right operand. For instance, ensuring the oxygen level is at or below 75%: `oxygen_level <= 75` returns `True`.                           |
| `>=`       | Greater than equal | `shield_power >= 90` is `True`   | The `>=` operator checks if the value of the left operand is greater than or equal to the value of the right operand. For example, confirming if the shield power is at least 90%: `shield_power >= 90` returns `True`.                        |
| `==`       | Equal              | `current_speed == max_speed` is `True` | The `==` operator checks if the value of two operands is equal. For instance, verifying if the current speed matches the maximum speed: `current_speed == max_speed` returns `True`.                                                                |
| `!=`       | Not equal          | `cargo_weight != max_capacity` is `True`   | The `!=` operator checks if the value of two operands is not equal. For example, checking if the cargo weight is different from the maximum capacity: `cargo_weight != max_capacity` returns `True`.                                                                          |

Here's an example of comparison operators in action.

> NOTE: Comparison operators are usually used for if-else statements, but they can have more applications apart from that.

```python
# Define variables
spaceship_speed = 6  # in warp units
speed_of_light = 7  # in warp units
asteroid_size = 6  # in km
shield_radius = 7  # in km
fuel_level = 6  # in units
min_fuel_required = 7  # in units
distance_to_star = 6  # in light-years
distance_to_planet = 7  # in light-years
crew_members = 6  # number of crew members
escape_pods = 7  # number of escape pods
alien_signals = 6  # number of alien signals detected
planets_scanned = 7  # number of planets scanned

# Less than 
print("Is the spaceship's speed (6 warp units) less than the speed of light (7 warp units)?", spaceship_speed < speed_of_light) # Prints True

# Greater than
print("Is the asteroid's size (6 km) greater than the spaceship's shield radius (7 km)?", asteroid_size > shield_radius) # Prints False

# Less than equal
print("Is the fuel level (6 units) less than or equal to the minimum required for a safe journey (7 units)?", fuel_level <= min_fuel_required) # Prints True

# Greater than equal
print("Is the distance to the nearest star (6 light-years) greater than or equal to the distance to the nearest planet (7 light-years)?", distance_to_star >= distance_to_planet) # Prints False

# Equal
print("Is the number of crew members on the spaceship (6) equal to the number of escape pods available (7)?", crew_members == escape_pods) # Prints False

# Not equal
print("Is the number of alien signals detected (6) not equal to the number of planets scanned (7)?", alien_signals != planets_scanned) # Prints True
```

**Tabitha**: "Alien signals, I wonder if we will encounter any"

### Exercise - calculate distance between coordinates

**Ship**: "Here's a tip, Tabitha. If you ever encounter alien signals, make sure to scan the planets nearby. In fact, let's do a little programming exercises: space is in 3D how far is it between the coordinates (1, 2, 3) and (4, 5, 6)?"

Answer: The distance between two points in 3D space can be calculated using the formula: `sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)`. In this case, the distance between the coordinates (1, 2, 3) and (4, 5, 6) would be `sqrt((4 - 1)^2 + (5 - 2)^2 + (6 - 3)^2) = sqrt(3^2 + 3^2 + 3^2) = sqrt(9 + 9 + 9) = sqrt(27 + 9) = sqrt(36) = 6`.

Code the above in Python and run it in your terminal.

[Exercise solution](./code/exercise.py)

### Assignment Operators

**Ship**: As the name suggests, Assignment operators in Python assign values to variables. But you can compound the assignment operators with arithmetic operators to perform more complex operations.

Let's take a look at the assignment operators generally used in Python:

| Operator |           Name          |     Example    | Result  | Description                                                                                                                                                                                                                              |
|:--------:|:-----------------------:|:--------------:|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `=`        | Assign                  | distance_to_black_hole `=` 1000          | distance_to_black_hole is 1000  | The `=` operator assigns a value to a variable. Here the distance to a black hole is being assigned to the variable `distance_to_black_hole`.                                                                                                                                    |
| `+=`       | Add and assign          | distance_to_black_hole `=` 1000; distance_to_black_hole `+=` 200  | distance_to_black_hole is 1200  | The `+=` operator will add the later value to the existing value of `distance_to_black_hole`. The initial distance is `1000`, and `distance_to_black_hole += 200` means `200` will be added to the existing value, resulting in `1200`.              |
| `-=`       | Subtract and assign     | asteroid_belt_distance `=` 500; asteroid_belt_distance `-=` 100  | asteroid_belt_distance is 400  | The `-=` operator means subtracting the later value from the existing value of `asteroid_belt_distance`. The initial distance is `500`, and `asteroid_belt_distance -= 100` means `100` will be subtracted, resulting in `400`.  |
| `*=`       | Multiply and assign     | ship_speed `=` 2; ship_speed `*=` 3  | ship_speed is 6  | The `*=` operator means it will multiply the later value to the existing value of `ship_speed`. The initial speed is `2`, and `ship_speed *= 3` means `3` will be multiplied by the existing value, resulting in `6`.    |
| `/=`       | Divide and assign       | fuel_reserve `=` 400; fuel_reserve `/=` 2  | fuel_reserve is 200  | The `/=` operator will divide the later value to the existing value of `fuel_reserve`. The initial reserve is `400`, and `fuel_reserve /= 2` means `2` will divide the existing value, resulting in `200`.         |
| `//=`      | Floor divide and assign | time_to_nearest_planet `=` 9; time_to_nearest_planet `//=` 2 | time_to_nearest_planet is 4  | The `//=` operator means it will floor divide the later value to the existing value of `time_to_nearest_planet`. The initial time is `9`, and `time_to_nearest_planet //= 2` means the result of floor division is `4`. |
| `%=`       | Modulus assign          | remaining_energy `=` 15; remaining_energy `%=` 4 | remaining_energy is 3  | The `%=` operator means it will divide the later value to the existing value of `remaining_energy` and store the remainder result in `remaining_energy`. The initial energy is `15`, and it will be divided by `4`, leaving a remainder of `3`.          |
| `**=`      | Power assign            | shield_strength `=` 2; shield_strength `**=` 3 | shield_strength is 8 | The `**=` operator means it will raise the existing value of `shield_strength` to the power of the later value. The initial strength is `2`, and `shield_strength **= 3` means `2` will be raised to the power of `3`, resulting in `8`.                                                                                                               |

> [!INFO]
> A black hole is a region of spacetime where gravity is so strong that nothing—no particles or even electromagnetic radiation such as light—can escape from it. The boundary of the region from which no escape is possible is called the event horizon.

Look at the example below to understand the implementation of Assignment operators:

```python
# Initialize a variable
black_hole_mass = 100
print("Initial mass of the black hole:", black_hole_mass)  # Output result -> Initial mass of the black hole: 100

# += operator
black_hole_mass += 5
print("Mass of the black hole after absorbing 5 units of matter:", black_hole_mass)  # Output result -> Mass of the black hole after absorbing 5 units of matter: 105

# -= operator
black_hole_mass -= 3
print("Mass of the black hole after ejecting 3 units of matter:", black_hole_mass)  # Output result -> Mass of the black hole after ejecting 3 units of matter: 102

# *= operator
black_hole_mass *= 2
print("Mass of the black hole after merging with another black hole of equal size:", black_hole_mass)  # Output result -> Mass of the black hole after merging with another black hole of equal size: 204

# /= operator
black_hole_mass /= 4
print("Mass of the black hole after losing 75% of its mass to a quasar jet:", black_hole_mass)  # Output result -> Mass of the black hole after losing 75% of its mass to a quasar jet: 51.0

# //= operator
black_hole_mass //= 3
print("Mass of the black hole after being divided into 3 smaller black holes:", black_hole_mass)  # Output result -> Mass of the black hole after being divided into 3 smaller black holes: 17.0

# %= operator
asteroid_mass = 2
remaining_mass = black_hole_mass % asteroid_mass
print("Remaining mass of the black hole after distributing it among asteroids of 2 units each:", remaining_mass)  # Output result -> Remaining mass of the black hole after distributing it among asteroids of 2 units each: 1.0

# **= operator
quasar_energy = 3
black_hole_mass **= quasar_energy
print("Mass of the black hole after being amplified by the energy of a quasar to the power of 3:", black_hole_mass)  # Output result -> Mass of the black hole after being amplified by the energy of a quasar to the power of 3: 1.0
```

And here is the output for the above code snippet:

> [!INFO]
> Quasars are extremely luminous and energetic sources of electromagnetic radiation. They are powered by accretion of material into supermassive black holes in the centers of galaxies.

## Operator Precedence

**Tabitha**: "I remember reading about black holes in astronomy class, but I never thought I'd be using them in a program. This is fascinating!"

**Ship**: "Glad to hear it, we need to talk about operator precedence next, that is the order of which operators are applied"

In Python, the operations don't all happen at once when we have an expression with multiple operations. Instead, they occur in a specific order based on their "rank" or "importance". This order is what we call "operator precedence". It's like doing math, where you do multiplication and division before addition and subtraction.

For Arithmetic operators, the PEMDAS rule is followed in precedence. Below is the precedence increasing from top to bottom.
P – Parentheses `()`
E – Exponentiation `**`
M – Multiplication `*`
D – Division `/`
A – Addition `+`
S – Subtraction `-`

> NOTE: Multiplication and Division have equal precedence. Similarly, Addition and Subtraction have equal precedence.

For Comparison operators, operations including less than (<), greater than (>), equal to (==), greater than or equal (>=), less than or equal (<=), not equal (!=), hold equal precedence. This follows with standard mathematical conventions, where an expression like a < b < c is interpreted as "b is greater than a and less than c".

These comparisons in Python result in `Boolean` values, returning either `True` or `False`. For instance:

```python
x = 5
y = 10
z = 15

print(x < y <= z)  # This would print: True
```

Another example:

```python
x = 5
y = 10
z = 6

print(x < y <= z)  # This would print: False
```

### Exercise - Operator Precedence

**Ship**: "Let's do another exercise, space-themed of course. Imagine you're navigating a spaceship through an asteroid field. You need to calculate the safest path by determining the total energy required to maneuver around the asteroids. The energy required is calculated using the following formula:"

```python
energy_required = (base_energy + asteroid_density * 2) ** 2 / (maneuverability + 1)
```

**Tabitha**: "Alright, Ship. So, I need to figure out the energy required based on the base energy, asteroid density, and the ship's maneuverability?"

**Ship**: "Exactly! But remember, operator precedence matters here. If you don't calculate the operations in the correct order, you might end up with the wrong energy requirement and crash into an asteroid!"

**Task**: Write a Python program to calculate the energy required for the spaceship to navigate the asteroid field. Use the following values:

- `base_energy = 10`
- `asteroid_density = 5`
- `maneuverability = 3`

Make sure to follow the correct operator precedence to avoid any miscalculations. Test your program and verify the result.

**Hint**: Use parentheses to ensure the operations are performed in the correct order if needed.

**Ship**: "Good luck, Captain Tabitha! The safety of the crew depends on your calculations."

[Exercise solution](./code/exercise2.py)

## Assignment

*Ok, let's see, Tabitha taking her time reading a laminated ships manual. We need to tread carefully here, not too much, not too little, remember multiplication effect, consider the absorber she muttered*

Your job is to reroute energy from the working bay to the engines. However, this needs to be done carefully, too little and you blow a fuse, too much and you risk damaging the engines. You need to calculate the amount of energy to reroute and ensure it is within the safe limits. Min and Max values are provided below:

- Engine Min value: 10
- Engine Max value: 100
- Energy to reroute: 50

The rerouting equation can best be described as:

> engine_effect = ((taking_energy + 3) * 5) / 4

> Remember, you need to leave the working bay with at least 10 units of energy.

Write a program that calculates the amount of energy to reroute. Ensure you run the program with safe input.

## Solution

[Solution](./solution.py)

## Quiz

**Question**. You have three integer variables x, y and z. If you perform x + y - z, would the result be different from y - z + x?

**Question**. Can you make a difference in the calculation sequence using parentheses with the integers? eg, 5 - (3 + 2)

**Question**. Would addition have higher precedence over subtraction?

[Solution quiz](./solutions/solution-quiz.md)

## Summary

In this chapter, we learned about operators in Python, including arithmetic, comparison, and assignment operators. We also explored operator precedence and how to use these operators to perform calculations in a spaceship navigation context. By understanding these concepts, we can effectively manipulate data and make decisions based on calculations in our programs.

We also practiced using operators in real-world scenarios, such as rerouting energy in a spaceship and calculating distances in space. This knowledge will be essential as we continue to develop our programming skills and tackle more complex challenges in the future.
