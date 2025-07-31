# Exercise 3 Solution
pressure_ok = True
hatch_locked = False
can_open_hatch = pressure_ok and not hatch_locked
print(can_open_hatch)  # True