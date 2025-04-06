import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(1)

def draw_circle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("blue")  # Set the color to blue
    t.begin_fill()   # Start filling the shape
    t.circle(50)
    t.end_fill()     # End filling the shape

# Bind the mouse click event
turtle.onscreenclick(draw_circle)

# Keep the window open
turtle.done()