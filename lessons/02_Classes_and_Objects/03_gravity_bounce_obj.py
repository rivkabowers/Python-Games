"""
Gravity bounce in Object Oriented style

This version of the gravity bounce program uses an object oriented style to
organize the code. The main game loop is in the Game class, and the player is
a separate class. This makes the code easier to read and understand, and
allows for more complex games with multiple objects.

"""
import pygame


class Colors:
    """Constants for Colors"""
    WHITE = (220, 172, 150)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (200, 73, 110)
    BROWN = (53,31,16)

class GameSettings:
    """Settings for the game"""
    width: int = 600
    height: int = 550
    gravity: float = 0.3
    player_start_x: int = 100
    player_start_y: int = None
    player_v_y: float = 0  # Initial y velocity
    player_v_x: float = 7  # Initial x velocity
    player_width: int = 20
    player_height: int = 20
    player_jump_velocity: float = 15


class Game:
    """Main object for the top level of the game. Holds the main loop and other
    update, drawing and collision methods that operate on multiple other
    objects, like the player and obstacles."""
    
    def __init__(self, settings: GameSettings):
        pygame.init()

        self.settings = settings
        self.running = True

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.clock = pygame.time.Clock()

        self.players = []

    def add_player(self, player):
        self.players.append(player)


    def run(self):
        """Main game loop"""

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            self.screen.fill(Colors.WHITE)

            for player in self.players:
                player.update()
                player.draw(self.screen)
                
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


class FirstEye:
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game):
        self.game = game
        settings = game.settings

        self.width = 55
        self.height = 50
      
        self.is_jumping = False
        self.v_jump = settings.player_jump_velocity

        self.y = settings.player_start_y if settings.player_start_y is not None else settings.height - self.height
        self.x = settings.player_start_x
        
        self.v_x = settings.player_v_x  # X Velocity
        self.v_y = settings.player_v_y  # Y Velocity

    def update(self):
        """Update player position, continuously jumping"""
        self.update_jump()
        self.update_y()
        self.update_x()

    def update_y(self):
        """Update the player's y position based on gravity and velocity"""
        self.v_y += self.game.settings.gravity  # Add gravity to the y velocity
        self.y += self.v_y  # Update the player's y position, based on the current velocity

        if self.y >= self.game.settings.height - self.height:
            self.y = self.game.settings.height - self.height
            self.v_y = 0
            self.is_jumping = False

    def update_x(self):
        """Update the player's x position based on horizontal velocity and bounce on edges"""
        self.x += self.v_x  # Update the player's x position based on the current velocity

        if self.x <= 0:
            self.x = 0
            self.v_x = -self.v_x
        elif self.x >= self.game.settings.width - self.width:
            self.x = self.game.settings.width - self.width
            self.v_x = -self.v_x

    def update_jump(self):
        """Handle the player's jumping logic"""
        
        if not self.is_jumping:
            self.v_y = -self.v_jump
            self.is_jumping = True

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.BLACK, (self.x, self.y, self.width, self.height))




class Eye:
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game):
        self.game = game
        settings = game.settings

        self.width = 55
        self.height = 50
       
        self.is_jumping = False
        self.v_jump = 16
        self.y = settings.player_start_y if settings.player_start_y is not None else settings.height - self.height
        self.x = settings.player_start_x
        
        self.v_x = 9 # X Velocity
        self.v_y = 11  # Y Velocity

    def update(self):
        """Update player position, continuously jumping"""
        self.update_jump()
        self.update_y()
        self.update_x()

    def update_y(self):
        """Update the player's y position based on gravity and velocity"""
        self.v_y += self.game.settings.gravity  # Add gravity to the y velocity
        self.y += self.v_y  # Update the player's y position, based on the current velocity

        if self.y >= self.game.settings.height - self.height:
            self.y = self.game.settings.height - self.height
            self.v_y = 0
            self.is_jumping = False

    def update_x(self):
        """Update the player's x position based on horizontal velocity and bounce on edges"""
        self.x += self.v_x  # Update the player's x position based on the current velocity

        if self.x <= 0:
            self.x = 0
            self.v_x = -self.v_x
        elif self.x >= self.game.settings.width - self.width:
            self.x = self.game.settings.width - self.width
            self.v_x = -self.v_x

    def update_jump(self):
        """Handle the player's jumping logic"""
        
        if not self.is_jumping:
            self.v_y = -self.v_jump
            self.is_jumping = True

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.BLACK, (self.x, self.y, self.width, self.height))




class Mouth:
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game):
        self.game = game
        settings = game.settings

        self.width = 80
        self.height = 20
      
        self.is_jumping = False
        self.v_jump = 13

        self.y = settings.player_start_y if settings.player_start_y is not None else settings.height - self.height
        self.x = 0
        
        self.v_x = 10 # X Velocity
        self.v_y = 20  # Y Velocity

    def update(self):
        """Update player position, continuously jumping"""
        self.update_jump()
        self.update_y()
        self.update_x()

    def update_y(self):
        """Update the player's y position based on gravity and velocity"""
        self.v_y += self.game.settings.gravity  # Add gravity to the y velocity
        self.y += self.v_y  # Update the player's y position, based on the current velocity

        if self.y >= self.game.settings.height - self.height:
            self.y = self.game.settings.height - self.height
            self.v_y = 0
            self.is_jumping = False

    def update_x(self):
        """Update the player's x position based on horizontal velocity and bounce on edges"""
        self.x += self.v_x  # Update the player's x position based on the current velocity

        if self.x <= 0:
            self.x = 0
            self.v_x = -self.v_x
        elif self.x >= self.game.settings.width - self.width:
            self.x = self.game.settings.width - self.width
            self.v_x = -self.v_x

    def update_jump(self):
        """Handle the player's jumping logic"""
        
        if not self.is_jumping:
            self.v_y = -self.v_jump
            self.is_jumping = True

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.BLUE, (self.x, self.y, self.width, self.height))



settings = GameSettings()
game = Game(settings)

p1 = FirstEye(game)
game.add_player(p1)

p2 = Mouth(game)
game.add_player(p2)

p3 = Eye(game)
game.add_player(p3)



game.run()
