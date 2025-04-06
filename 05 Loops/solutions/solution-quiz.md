**Question**: What is the output of the following spaceship navigation code?

```python
for i in range(3):
    print(f"Navigating to sector {i}")
```

**A**: The output is `Navigating to sector 0`, `Navigating to sector 1`, `Navigating to sector 2`.


**Question**: Why would I use a list comprehension over a for-loop in a spaceship's control system?

**A**: List comprehension is a more concise way to create a new list from an existing list. You would use it instead of a for-loop when you want to quickly generate a list, such as filtering sensor readings or mapping crew assignments.

**Question**: What do `break` and `continue` do in a spaceship's loop control system?

**A**: `break` halts the loop entirely, such as when an alien is detected and the search must stop. `continue` skips the current iteration, like bypassing a malfunctioning sensor and moving to the next one.