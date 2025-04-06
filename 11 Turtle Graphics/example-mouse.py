import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(1)

def draw_circle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(50)

# Bind the mouse click event
turtle.onscreenclick(draw_circle)

# Keep the window open
turtle.done()