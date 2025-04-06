import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
# Set up the clock
clock = pygame.time.Clock()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Set up the player ship
player_ship = pygame.Rect(400, 300, 50, 50)  # x, y, width, height
player_velocity_x = 0  # Horizontal velocity of the player ship

# Create the meteors
meteors = []
for _ in range(5):  # Create 5 meteors
    meteor_x = random.randint(0, 800)
    meteor_y = random.randint(0, 600)
    meteor_width = random.randint(20, 50)
    meteor_height = random.randint(20, 50)
    meteor = pygame.Rect(meteor_x, meteor_y, meteor_width, meteor_height)
    meteors.append(meteor)

# Main game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity_x = -5
            if event.key == pygame.K_RIGHT:
                player_velocity_x = 5

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_velocity_x = 0

    # Update game state
    player_ship.x += player_velocity_x  # Update player position based on velocity

    # Prevent the player ship from going off-screen
    if player_ship.x < 0:
        player_ship.x = 0
    if player_ship.x > 750:  # 800 - player_ship width
        player_ship.x = 750

    for meteor in meteors:
        meteor.y += 5  # Move the meteor down the screen
        if meteor.y > 600:  # If the meteor goes off the screen, reset its position
            meteor.y = 0
            meteor.x = random.randint(0, 800)

    # Draw everything
    screen.fill(BLACK)  # Clear the screen with black
    pygame.draw.rect(screen, WHITE, player_ship)  # Draw the player ship

    for meteor in meteors:
        pygame.draw.rect(screen, WHITE, meteor)  # Draw the meteors

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS