import pygame
import random

class Arcship:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 200, 200)  # x, y, width, height
        self.health = 100  # Health of the arcship
        self.speed = 0  # Speed of the arcship
        self.arcship_image = pygame.image.load("assets/arcship.png")
        self.arcship_image = pygame.transform.scale(self.arcship_image, (200, 200))

    def decrease_health(self):
        self.health -= 20

    def is_dead(self):
        return self.health <= 0

    def draw(self):
        self.screen.blit(self.arcship_image, (self.rect.x, self.rect.y))

    def is_colliding(self, other_rect):
        # Check for collision with another rectangle
        return self.rect.colliderect(other_rect)

    def reset(self):
        self.rect.x = 300
        self.rect.y = 400
        self.health = 100
        self.speed = 0  # Reset speed to 0

    def update(self):
        self.y += self.speed  # Update the arcship position based on speed

class Missile:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 5, 10)  # x, y, width, height
        self.speed = -1.5  # Move up the screen
        self.missile_image = pygame.image.load("assets/missile.png")
        self.missile_image = pygame.transform.scale(self.missile_image, (5, 10))

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.missile_image, (self.rect.x, self.rect.y))


class PlayerShip:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.player_ship_image = pygame.image.load("assets/player.png")
        self.player_ship_image = pygame.transform.scale(self.player_ship_image, (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)  # x, y, width, height
        self.health = 100  # Health of the player ship
        self.velocity = 0  # Horizontal velocity of the player ship

    def draw(self):
        self.screen.blit(self.player_ship_image, (self.rect.x, self.rect.y))

    def update(self):
        # Update the player ship position based on velocity
        self.rect.x += self.velocity

        # Prevent the player ship from going off-screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 750:
            self.rect.x = 750

    def reset(self):
        self.rect.x = 400
        self.rect.y = 300
        self.health = 100
        self.velocity = 0  # Reset velocity to 0


class Meteor:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 50, 50)  # x, y, width, height
        self.speed = 3  # Speed of the meteor
        self.meteor_image = pygame.image.load("assets/meteor_1.png")
        self.meteor_image = pygame.transform.scale(self.meteor_image, (50, 50))

    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 600:  # If the meteor goes off the screen, reset its position
            self.rect.y = 0
            self.rect.x = random.randint(0, 800)

    def reset(self):
        self.rect.y = random.randint(-600, -50)  # Reset meteor position off-screen
        self.rect.x = random.randint(0, 800)

    def draw(self):
        self.screen.blit(self.meteor_image, (self.rect.x, self.rect.y))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)


        print("creating player")
        self.player = PlayerShip(400, 300, self.screen)  # Create an instance of PlayerShip
        self.missiles = []  # List to store missiles

        print("Creating arcship")
        self.arc_ship_obj = Arcship(300, 400, self.screen)  # Create an instance of Arcship

        # Load sound
        print("Loading sound")
        pygame.mixer.init()
        pygame.mixer.music.load("assets/background-sound.mp3")
        pygame.mixer.music.play(-1)  # Play the music in a loop

        # load sound effect
        self.missile_sound = pygame.mixer.Sound("assets/missile.ogg")
        self.explosion_sound = pygame.mixer.Sound("assets/explosion.ogg")

        # Load background image
        self.background_image = pygame.image.load("assets/background.png")
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))  # Scale the background image to fit the screen

        self.meteors_destroyed = 0 
        self.meteors_to_destroy = 20  # Total meteors to destroy to win

        print("Creating meteors")
        # create meteors
        self.meteors = []
        for _ in range(5):  # Create 5 meteors

            meteor_x = random.randint(0, 800)
            meteor_y = random.randint(0, 600)

            meteor = Meteor(meteor_x, meteor_y, self.screen)
            self.meteors.append(meteor)

    def reset_game(self):    
        self.meteors_destroyed = 0
        self.arc_ship_obj.reset()  # Reset the arcship object

        # Reset the game state
        self.player.reset()

        for meteor in self.meteors:
            meteor.reset()

    def show_game_over_screen(self):
        # Show game over screen
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before resetting the game
        self.reset_game()

    
    def shoot_missile(self):
        # Create a new missile and add it to the list
        missile = Missile(self.player.rect.x + self.player.rect.width // 2, self.player.rect.y, self.screen)
        self.missiles.append(missile)
        self.missile_sound.play()  # Play the missile sound

    def show_victory_screen(self):
        # Show victory screen
        font = pygame.font.Font(None, 74)
        text = font.render("You Win!", True, (0, 255, 0))
        self.screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before exiting the game

    def display_remaining_meteors(self):
         # Display the remaining meteors to destroy
        font = pygame.font.Font(None, 36)
        text = font.render(f"Meteors Left: {self.meteors_to_destroy - self.meteors_destroyed}", True, self.WHITE)
        self.screen.blit(text, (600, 10))  # Display in the top-right corner

    def display_arcship_health(self):
        # display arcship health
        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Arcship Health: {self.arc_ship_obj.health}", True, self.WHITE)

        # show archship health as a bar in top center
        health_bar_width = 230
        health_bar_height = 30
        health_bar_x = (800 - health_bar_width) // 2
        health_bar_y = 10
        pygame.draw.rect(self.screen, self.RED, (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 1)  # Draw the border
        pygame.draw.rect(self.screen, (0, 255, 0), (health_bar_x, health_bar_y, health_bar_width * (self.arc_ship_obj.health / 100), health_bar_height))  # Draw the health bar
        self.screen.blit(health_text, (health_bar_x + 5, health_bar_y + 2))  # Display health text

    def if_game_won(self):
        return self.meteors_destroyed >= self.meteors_to_destroy

    def show_menu(self):
        menu_running = True
        font = pygame.font.Font(None, 74)
        while menu_running:
            self.screen.fill(self.BLACK)
            title_text = font.render("Arcship Game", True, self.WHITE)
            start_text = font.render("Press S to Start", True, self.WHITE)
            quit_text = font.render("Press Q to Quit", True, self.WHITE)

            self.screen.blit(title_text, (400 - title_text.get_width() // 2, 200))
            self.screen.blit(start_text, (400 - start_text.get_width() // 2, 300))
            self.screen.blit(quit_text, (400 - quit_text.get_width() // 2, 400))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        menu_running = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()

    def pause_game(self):
        paused = True
        font = pygame.font.Font(None, 74)
        while paused:
            self.screen.fill(self.BLACK)
            pause_text = font.render("Game Paused", True, self.WHITE)
            resume_text = font.render("Press Esc to Resume", True, self.WHITE)
            quit_text = font.render("Press Q to Quit", True, self.WHITE)

            self.screen.blit(pause_text, (400 - pause_text.get_width() // 2, 200))
            self.screen.blit(resume_text, (400 - resume_text.get_width() // 2, 300))
            self.screen.blit(quit_text, (400 - quit_text.get_width() // 2, 400))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()

    def run(self):
        print("Game started")
        self.show_menu()  # Show the menu before starting the game

        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False # stops game loop

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.velocity = -5
                    if event.key == pygame.K_RIGHT:
                        self.player.velocity = 5
                    if event.key == pygame.K_SPACE:
                        self.shoot_missile()
                    if event.key == pygame.K_ESCAPE:  # Pause the game when Esc is pressed
                        self.pause_game()

                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        self.player.velocity = 0

            # Update game state
            self.player.update()  

            for meteor in self.meteors:
                meteor.update()  # Update the meteor position

            self.screen.fill(self.BLACK)  # Clear the screen with black
          
            self.screen.blit(self.background_image, (0, 0)) 
            self.player.draw()  # Draw the player ship
            self.arc_ship_obj.draw()  # Draw the arcship object  

            for meteor in self.meteors:
                meteor.draw()

                if self.player.rect.colliderect(meteor.rect):
                    self.show_game_over_screen()
                
                if self.arc_ship_obj.is_colliding(meteor.rect):
                    # reposition the meteor
                    meteor.reset()
                    self.explosion_sound.play() 
                    self.arc_ship_obj.decrease_health()  
                    
                    if self.arc_ship_obj.is_dead():
                        print("Arcship destroyed!")
                        self.show_game_over_screen()
            
                for missile in self.missiles:
                    missile.draw()  
                    missile.update()  

                    # check it more than once, missile and meteors are moving fast
                    for _ in range(10):
                    # Check for collisions with meteors
                        if missile.rect.colliderect(meteor):
                            self.explosion_sound.play() 
                            meteor.reset()

                            if missile in self.missiles: 
                                self.missiles.remove(missile)  

                            self.meteors_destroyed += 1 
                     
                            if self.if_game_won():
                                self.show_victory_screen()
                                # display "press any key to continue"
                                font = pygame.font.Font(None, 74)
                                text = font.render("Press \"C\" key to continue", True, (0, 255, 0))
                                self.screen.blit(text, (400 - text.get_width() // 2, 400 - text.get_height() // 2))
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
                                                self.reset_game()
                            
                            break

            self.display_remaining_meteors()  
            self.display_arcship_health()  

            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

game = Game()

game.run()