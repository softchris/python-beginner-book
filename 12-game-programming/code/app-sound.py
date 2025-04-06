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
RED = (255, 0, 0)
# Load images
player_ship_image = pygame.image.load("assets/player.png")
meteor_image = pygame.image.load("assets/meteor_1.png")
# Scale images
player_ship_image = pygame.transform.scale(player_ship_image, (50, 50))
meteor_image = pygame.transform.scale(meteor_image, (50, 50))

# Load sound
# pygame.mixer.init()
# pygame.mixer.music.load("assets/music.mp3")
# pygame.mixer.music.play(-1)  # Play the music in a loop

# load sound effect
missile_sound = pygame.mixer.Sound("assets/missile.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.ogg")
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

class Missile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)  # x, y, width, height
        self.speed = -2  # Move up the screen

    def update(self):
        self.rect.y += self.speed
missiles = []  # List to store missiles
def shoot_missile():
    # Create a new missile and add it to the list
    missile = Missile(player_ship.x + player_ship.width // 2, player_ship.y)
    missiles.append(missile)
    missile_sound.play()  # Play the missile sound
 
def reset_game():
    # Reset the game state
    player_ship.x = 400
    player_ship.y = 300
    for meteor in meteors:
        meteor.y = random.randint(-600, -50)  # Reset meteor position off-screen
        meteor.x = random.randint(0, 800)
def show_game_over_screen():
    # Show game over screen
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds before resetting the game
    reset_game()

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
            if event.key == pygame.K_SPACE:
                shoot_missile()

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
    screen.blit(player_ship_image, (player_ship.x, player_ship.y))  # Draw the player ship

    for meteor in meteors:
        screen.blit(meteor_image, (meteor.x, meteor.y))  # Draw the meteors

        if player_ship.colliderect(meteor):
            # Handle collision
            print("Collision detected!")
            # decide what do to
        
            # show game over screen
            show_game_over_screen()
        
       
        for missile in missiles:
            pygame.draw.rect(screen, (0, 0, 255), missile.rect)  # Draw the missile
            missile.update()  # Update the missile position

            # check it twice, missile and meteors are moving fast
            for _ in range(2):
            # Check for collisions with meteors
                if missile.rect.colliderect(meteor):
                    explosion_sound.play()  # Play explosion sound
                        
                    # reposition the meteor
                    meteor.y = random.randint(-600, -50)  # Reset meteor position off-screen
                    meteor.x = random.randint(0, 800)

                    if missile in missiles:  # Ensure the missile is still in the list
                        missiles.remove(missile)  # Remove the missile
                    break
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS