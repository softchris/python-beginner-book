# import random module
import random

class Dice:
    # constructor
    def __init__(self,sides):
        self.sides = sides
    def throw(self):
        # get random number between 1 and sides
        return random.randint(1,self.sides)

dice = Dice(6)
dice.throw()
dice.throw()
dice.throw()

# create for loop to throw dice 3 times
for i in range(3):
    print(dice.throw())




