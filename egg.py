import pygame
import os

EGG_IMAGE = pygame.image.load(os.path.join('assets', 'pixel-egg.png'))
EGG = pygame.transform.scale(EGG_IMAGE, (100, 76))

BROKEN_EGG_IMAGE = pygame.image.load(os.path.join('assets', 'broken-egg.png'))
BROKEN_EGG = pygame.transform.scale(BROKEN_EGG_IMAGE, (100, 76))


class Egg():
    def __init__(self, screen, x, y = 730):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 100
        self.height = 76

    def update_position(self, x):
        self.x = x
    
    def draw_egg(self, x = 0):
        self.screen.blit(EGG, (self.x, self.y))
