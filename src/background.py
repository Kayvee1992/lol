import pygame
import os

BG_IMAGE = pygame.image.load(os.path.join('assets', 'highway-background.jpeg'))

class Background():
    def __init__(self, screen, width, height):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height

    def draw_bg(self):
        BG = pygame.transform.scale(BG_IMAGE, (self.width, self.height))
        self.screen.blit(BG, (0,0))