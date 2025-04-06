import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(1)

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

# Bind the keys
turtle.listen()
turtle.onkey(move_forward, "w")
turtle.onkey(move_backward, "s")
turtle.onkey(turn_left, "a")
turtle.onkey(turn_right, "d")

# Keep the window open
turtle.done()