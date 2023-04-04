import pygame

class Car():
    # Create a constructor for the car
    def __init__(self, screen, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = 2
        self.screen = screen

    def draw_car(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.rect.y += self.velocity

    