import turtle

# Create a turtle object
spaceship = turtle.Turtle()
spaceship.speed(1)

def move_forward():
    spaceship.forward(10)

def move_backward():
    spaceship.backward(10)

def turn_left():
    spaceship.left(10)

def turn_right():
    spaceship.right(10)


# Create a screen object
screen = turtle.Screen()

# Bind the keys
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

# Keep the window open
screen.mainloop()