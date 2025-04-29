import pygame
class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store Decimal Value of Ship's Positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement_Flags
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def update(self):
        if self.move_right == True:
            self.x += self.settings.ship_speed
        if self.move_left == True:
            self.x -= self.settings.ship_speed
        if self.move_up == True:
            self.y -= self.settings.ship_speed
        if self.move_down == True:
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)