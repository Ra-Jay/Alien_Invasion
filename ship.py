import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        ''' Initialize the ship '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #  Load the ship image and get rect
        self.image = pygame.image.load('Desktop/Python/Projects/Alien Invasion/Images/ship1.png')
        self.rect = self.image.get_rect()

        #  Start each new ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal
        self.x = float(self.rect.x)

        #Movement flags
        self.moving_right = False 
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        ''' Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)