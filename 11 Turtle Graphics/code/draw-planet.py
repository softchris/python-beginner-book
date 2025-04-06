import turtle

# Create a turtle object
planet = turtle.Turtle()
planet.speed(1)

def draw_planet(x, y):
    planet.penup()
    planet.goto(x, y)
    planet.pendown()
    planet.color("blue")  # Set the color to blue for the planet
    planet.begin_fill()   # Start filling the shape
    planet.circle(50)     # Draw the planet
    planet.end_fill()     # End filling the shape
   

# Bind the mouse click event
turtle.onscreenclick(draw_planet)

# Keep the window open
turtle.done()