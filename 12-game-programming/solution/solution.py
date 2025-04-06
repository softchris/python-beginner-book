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
arcship_image = pygame.image.load("assets/arcship.png")
missile_image = pygame.image.load("assets/missile.png")

background_image = pygame.image.load("assets/background.png")
background_image = pygame.transform.scale(background_image, (800, 600))  # Scale the background image to fit the screen

# Scale images
player_ship_image = pygame.transform.scale(player_ship_image, (50, 50))
meteor_image = pygame.transform.scale(meteor_image, (50, 50))

arcship_image = pygame.transform.scale(arcship_image, (200, 200))
missile_image = pygame.transform.scale(missile_image, (5, 10))

meteors_destroyed = 0 
meteors_to_destroy = 10  # Total meteors to destroy to win

def reset_game():
    global meteors_destroyed
    
    meteors_destroyed = 0
    arc_ship_obj.reset()  # Reset the arcship object

    # Reset the game state
    player_ship.x = 400
    player_ship.y = 300
    for meteor in meteors:
        meteor.y = random.randint(-600, -50)  # Reset meteor position off-screen
        meteor.x = random.randint(0, 800)

def show_victory_screen():
    # Show victory screen
    font = pygame.font.Font(None, 74)
    text = font.render("You Win!", True, (0, 255, 0))
    screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds before exiting the game

# Load sound
pygame.mixer.init()
pygame.mixer.music.load("assets/background-sound.mp3")
pygame.mixer.music.play(-1)  # Play the music in a loop

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


arc_ship = pygame.Rect(300, 400, 200, 200)  # x, y, width, height


class Arcship:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 200, 200)  # x, y, width, height
        self.health = 100  # Health of the arcship
        self.speed = 0  # Speed of the arcship

    def draw(self, screen):
        screen.blit(arcship_image, (self.rect.x, self.rect.y))

    def reset(self):
        self.rect.x = 300
        self.rect.y = 400
        self.health = 100
        self.speed = 0  # Reset speed to 0

    def update(self):
        self.y += self.speed  # Update the arcship position based on speed

class Missile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)  # x, y, width, height
        self.speed = -1.5  # Move up the screen

    def update(self):
        self.rect.y += self.speed
missiles = []  # List to store missiles

arc_ship_obj = Arcship(300, 400)  # Create an instance of Arcship

def shoot_missile():
    # Create a new missile and add it to the list
    missile = Missile(player_ship.x + player_ship.width // 2, player_ship.y)
    missiles.append(missile)
    missile_sound.play()  # Play the missile sound
   
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
        meteor.y += 3  # Move the meteor down the screen
        if meteor.y > 600:  # If the meteor goes off the screen, reset its position
            meteor.y = 0
            meteor.x = random.randint(0, 800)

    # Draw everything
    screen.fill(BLACK)  # Clear the screen with black
    screen.blit(background_image, (0, 0))  # Draw the background image

    screen.blit(player_ship_image, (player_ship.x, player_ship.y))  # Draw the player ship

      # draw arcship
    arc_ship_obj.draw(screen)  # Draw the arcship object  

    for meteor in meteors:
        screen.blit(meteor_image, (meteor.x, meteor.y))  # Draw the meteors

        if player_ship.colliderect(meteor):
            # Handle collision
            print("Collision detected!")
            # decide what do to
        
            # show game over screen
            show_game_over_screen()
        
        if arc_ship.colliderect(meteor):
            # reposition the meteor
            meteor.y = random.randint(-600, -50)
            meteor.x = random.randint(0, 800)
            explosion_sound.play()  # Play explosion sound

            arc_ship_obj.health -= 20  # Decrease arcship health
            
            if arc_ship_obj.health <= 0:
                # Handle arcship destruction
                print("Arcship destroyed!")
                show_game_over_screen()
       
        for missile in missiles:
            screen.blit(missile_image, (missile.rect.x, missile.rect.y))  # Draw the missile
            # pygame.draw.rect(screen, (0, 0, 255), missile.rect)  # Draw the missile
            missile.update()  # Update the missile position

            # check it twice, missile and meteors are moving fast
            for _ in range(10):
            # Check for collisions with meteors
                if missile.rect.colliderect(meteor):
                    explosion_sound.play()  # Play explosion sound
                        
                    # reposition the meteor
                    meteor.y = random.randint(-600, -50)  # Reset meteor position off-screen
                    meteor.x = random.randint(0, 800)

                    if missile in missiles:  # Ensure the missile is still in the list
                        missiles.remove(missile)  # Remove the missile

                    meteors_destroyed += 1  # Increment the count of destroyed meteors
                    # Check if the game is won
                    if meteors_destroyed >= meteors_to_destroy:
                        show_victory_screen()
                        # display "press any key to continue"
                        font = pygame.font.Font(None, 74)
                        text = font.render("Press \"C\" key to continue", True, (0, 255, 0))
                        screen.blit(text, (400 - text.get_width() // 2, 400 - text.get_height() // 2))
                        pygame.display.flip()
                        waiting = True

                        while waiting:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    waiting = False
                                    running = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_c:
                                        waiting = False
                                        reset_game()
                    
                    break

    # Display the remaining meteors to destroy
    font = pygame.font.Font(None, 36)
    text = font.render(f"Meteors Left: {meteors_to_destroy - meteors_destroyed}", True, WHITE)
    screen.blit(text, (600, 10))  # Display in the top-right corner

    # display arcship health
    health_text = font.render(f"Arcship Health: {arc_ship_obj.health}", True, WHITE)

    # show archship health as a bar in top center
    health_bar_width = 230
    health_bar_height = 30
    health_bar_x = (800 - health_bar_width) // 2
    health_bar_y = 10
    pygame.draw.rect(screen, RED, (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 1)  # Draw the border
    pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_bar_width * (arc_ship_obj.health / 100), health_bar_height))  # Draw the health bar
    screen.blit(health_text, (health_bar_x + 5, health_bar_y + 2))  # Display health text


    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS