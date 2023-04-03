import pygame


class Road(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, border_color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.border_width = 4
        self.height = height
        self.width = width
        self.color = color
        self.border_color = border_color
        self.add_border()

    def add_border(self):
        pygame.draw.rect(self.image, self.border_color, (0, 0, self.width, self.height), self.border_width)  
        

