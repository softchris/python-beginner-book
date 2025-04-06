import turtle
import tkinter as tk
from tkinter import simpledialog

# Set the background color to black
turtle.bgcolor("black")

# Create a turtle object
drawer = turtle.Turtle()
drawer.speed(1)

def draw_planet(x, y, color, size, draw_ring):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color(color)  # Set the color for the planet
    drawer.begin_fill()  # Start filling the shape
    drawer.circle(size)  # Draw the planet
    drawer.end_fill()    # End filling the shape

    if draw_ring:
        # Draw the outer ring
        drawer.penup()
        drawer.goto(x, y - 10)  # Move to the center of the planet
        drawer.pendown()
        drawer.color("red")  # Set the color to red for the ring
        drawer.circle(size + 10)  # Draw the outer ring
        drawer.penup()
        drawer.goto(0, 0)     # Move back to the center
        drawer.pendown()
        drawer.color("black")  # Set the color back to black

def on_click(x, y):
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    input_data = simpledialog.askstring(
        "Input", 
        "Enter the color, size, and ring (yes/no) separated by commas (e.g., red,50,yes):"
    )

    if input_data:
        try:
            color, size, draw_ring = [item.strip() for item in input_data.split(",")]
            size = int(size)
            draw_ring = draw_ring.lower() == "yes"
            draw_planet(x, y, color, size, draw_ring)
        except ValueError:
            print("Invalid input format. Please try again.")

# Bind the mouse click event
turtle.onscreenclick(on_click)
# Keep the window open
turtle.done()
