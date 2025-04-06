import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# how do you set title on a pygame window?
pygame.display.set_caption("Simple Game")

# screen.title("Simple Game")

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    # TODO: Update game objects here

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen with black
    # Draw your game objects here

    pygame.display.flip()  # Update the display