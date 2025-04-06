import turtle
import tkinter as tk
from tkinter import simpledialog
import random

# Set the background color to black
turtle.bgcolor("black")

# Create a turtle object
drawer = turtle.Turtle()
drawer.speed(1)

def draw_planet(x, y, color, size, draw_ring, name="planet"):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color(color)  # Set the color for the planet
    drawer.begin_fill()  # Start filling the shape
    drawer.circle(size)  # Draw the planet
    drawer.end_fill()    # End filling the shape
    
    # Add a label for the planet
    drawer.penup()
    drawer.goto(x, y - 10 + size)  # Move to the center
    drawer.pendown()
    drawer.color("white")  # Set the color for the label
    drawer.write(name, align="center", font=("Arial", 12, "normal"))  # Write the name of the planet

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


def draw_asteroid(x, y, size, name="asteroid"):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color("brown")  # Asteroids are always brown
    drawer.begin_fill()

    # Draw an uneven polygon to simulate an asteroid
    num_sides = random.randint(5, 10)  # Random number of sides
    angle = 360 / num_sides
    for _ in range(num_sides):
        offset = random.randint(-size // 4, size // 4)  # Add irregularity
        drawer.forward(size + offset)
        drawer.left(angle)

    drawer.end_fill()

def on_click(x, y):
    root = tk.Tk()
    # root.withdraw()  # Hide the root window

    root.deiconify()  # Show the root window

    # Create the modal dialog
    tk.Label(root, text="Select Object Type:").pack()
    object_type_var = tk.StringVar(value="Planet")
    tk.OptionMenu(root, object_type_var, "Planet", "Asteroid").pack()

    tk.Label(root, text="Select Size:").pack()
    size_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
    size_slider.pack()

    tk.Label(root, text="Type Color:").pack()
    color_var = tk.StringVar(value="red")
    color_picker = tk.Entry(root, textvariable=color_var)
    color_picker.pack()

    def update(res):
      before = res.get() 
      print(f"Present value {before}")
      res.set(not before)
      print(f"Updated value {res.get()}") 

    ring_var = tk.BooleanVar(value=False)
    ch = tk.Checkbutton(root, text="Has Ring (for Planet)", variable=ring_var, command= lambda: update(ring_var))
    ch.pack()  # Ensure the Checkbutton is packed to display
   
   # Default to checked

    tk.Label(root, text="Name:").pack()
    name_var = tk.StringVar(value="<placeholder name>")
    name_picker = tk.Entry(root, textvariable=name_var)
    name_picker.pack()

    def submit():
        chosen_type = object_type_var.get()
        chosen_size = size_slider.get()
        chosen_color = color_picker.get()
        chosen_ring = ring_var.get()
        chosen_label = name_picker.get()
        if chosen_type == "Planet":
            print(f"Drawing a {chosen_color} planet of size {chosen_size} with ring: {chosen_ring}")
            draw_planet(x=x, y=y, color=chosen_color, size=chosen_size, draw_ring= chosen_ring, name=chosen_label)
        elif chosen_type == "Asteroid":
            print(f"Drawing an asteroid of size {chosen_size}")
            draw_asteroid(x, y, chosen_size) 
        root.destroy()

    tk.Button(root, text="Submit", command=submit).pack()

    root.mainloop()
        

# Create a screen object
screen = turtle.Screen()

screen.listen()  # Enable the screen to listen for key presses

# Bind the mouse click event
turtle.onscreenclick(on_click)

# Keep the window open
turtle.done()
