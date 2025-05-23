import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
    
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Test Alien Invasion with Undertale Heart")

        self.ship = Ship(self)


    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = True
                elif event.key == pygame.K_UP:
                    self.ship.move_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.move_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = False
                elif event.key == pygame.K_UP:
                    self.ship.move_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.move_down = False


    
    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__  == '__main__':

    ai = AlienInvasion()
    ai.run_game()