import random
import pygame
import os
class Car():
    # Create a constructor for the car
    def __init__(self, screen, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = 2
        self.screen = screen
        car_number = random.randint(1, 2)
        car_name = 'car_' + str(car_number) + '.png';
        car_image = pygame.image.load(os.path.join('assets', car_name))
        self.car = pygame.transform.scale(car_image, (self.width, self.height))

    def draw_car(self):
        self.screen.blit(self.car, (self.rect.x, self.rect.y))


    def update(self):
        self.rect.y += self.velocity

    