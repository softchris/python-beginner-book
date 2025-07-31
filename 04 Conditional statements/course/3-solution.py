# Exercise 3 Solution
crew_awake = True
crew_busy = False

if crew_awake and not crew_busy:
    print("Crew is ready for duty.")
elif crew_awake and crew_busy:
    print("Crew is busy.")
else:
    print("Crew is resting.")