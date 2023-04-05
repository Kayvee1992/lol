import pygame
import os

EGG_WIDTH = 35
EGG_HEIGHT = 45

EGG_IMAGE = pygame.image.load(os.path.join('assets', 'pixel-egg.png'))
EGG = pygame.transform.scale(EGG_IMAGE, (EGG_WIDTH, EGG_HEIGHT))

BROKEN_EGG_IMAGE = pygame.image.load(os.path.join('assets', 'broken-egg.png'))
BROKEN_EGG = pygame.transform.rotate(pygame.transform.scale(BROKEN_EGG_IMAGE, (EGG_WIDTH, EGG_HEIGHT)), 90)


class Egg():

    def __init__(self, screen, x, y = 800 - EGG_HEIGHT - 10):
        super().__init__()
        self.screen = screen
        width = EGG_WIDTH
        height = EGG_HEIGHT
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height

    def update_position(self, x):
        self.rect.x = x
    
    def draw_egg(self, x = 0):
        # pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        self.screen.blit(EGG, (self.rect.x, self.rect.y))

    def draw_broken_egg(self, x = 0):
        self.screen.blit(BROKEN_EGG, (self.rect.x, self.rect.y))
        
        

