def read_gravity():
    level = int(input("Enter the gravity level: "))
    return level

gravity_level = read_gravity()

if gravity_level > 10:
    print("Gravity is dangerously high! Immediate action required.")
elif gravity_level > 3:
    print("Gravity is at operational levels but needs monitoring.")
else:
    print("Gravity is too low! Adjustments are necessary to stabilize the environment.")