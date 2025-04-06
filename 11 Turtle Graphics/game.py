import turtle

# Create a turtle object for the player
t = turtle.Turtle()
t.shape("turtle")

# Create a list of obstacles (for demonstration purposes, we'll create one obstacle)
obstacles = [turtle.Turtle(shape="square") for _ in range(1)]
for obstacle in obstacles:
    obstacle.penup()
    obstacle.goto(300, 0)

# Create a turtle object for displaying points
points_turtle = turtle.Turtle()
points_turtle.hideturtle()
points_turtle.penup()
points_turtle.goto(200, 200)

# Initialize points
points = 0

# Define the movement functions
def move_up():
    y = t.ycor()
    t.sety(y + 20)

def move_down():
    y = t.ycor()
    t.sety(y - 20)

# Function to reset the game
def reset_game():
    global game_running, points
    t.clear()
    t.goto(0, 0)
    for obstacle in obstacles:
        obstacle.goto(300, 0)
    points = 0
    update_points()
    game_running = True
    main_game_loop()

# Function to update points
def update_points():
    global points
    points += 10
    points_turtle.clear()
    points_turtle.write(f"Points: {points}", align="center", font=("Arial", 16, "normal"))
    if game_running:
        turtle.ontimer(update_points, 5000)  # Update points every 5 seconds

# Main game loop function
def main_game_loop():
    global game_running
    while game_running:
        for obstacle in obstacles:
            x = obstacle.xcor()
            obstacle.setx(x - 10)

            if obstacle.xcor() < -300:
                obstacle.goto(300, 0)

            if t.distance(obstacle) < 20:
                # Show game over message
                t.goto(0, 0)
                t.write("Game Over", align="center", font=("Arial", 24, "normal"))
                
                # Stop the game
                game_running = False
               

                break

# Bind the keys
turtle.listen()
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.onkey(reset_game, "Return")  # Bind Enter key to reset the game

# Start the game
game_running = True
update_points()  # Start updating points
main_game_loop()

# Keep the window open
turtle.done()