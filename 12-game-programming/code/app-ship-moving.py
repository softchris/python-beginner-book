import pygame

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

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_ship.x -= 5
            if event.key == pygame.K_RIGHT:
                player_ship.x += 5
            if event.key == pygame.K_UP:
                player_ship.y -= 5
            if event.key == pygame.K_DOWN:
                player_ship.y += 5

    # Update game state

    # Draw everything
    screen.fill(BLACK)  # Clear the screen with black
    pygame.draw.rect(screen, WHITE, player_ship)  # Draw the player ship

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
