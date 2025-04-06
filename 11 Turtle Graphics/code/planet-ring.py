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

    # Draw the outer ring
    planet.penup()
    planet.goto(x, y - 10)  # Move to the center of the planet
    planet.pendown()
    planet.color("red")  # Set the color to red for the ring
    planet.circle(60)     # Draw the outer ring
    planet.penup()
    planet.goto(0, 0)     # Move back to the center
    planet.pendown()
    planet.color("black")  # Set the color back to black
# Bind the mouse click event
turtle.onscreenclick(draw_planet)
# Keep the window open
turtle.done()