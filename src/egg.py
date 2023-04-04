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
        width = 100
        height = 76
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height

    def update_position(self, x):
        self.rect.x = x
    
    def draw_egg(self, x = 0):
        self.screen.blit(EGG, (self.rect.x, self.rect.y))
