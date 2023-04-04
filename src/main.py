from background import Background
import pygame
from egg import *
from road import Road

# Constants

FPS = 60
VELOCITY = 2

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

# Dimensions and positions
WIDTH = 600
HEIGHT = 800
ROAD_WIDTH = 200
ROAD_X = 200
ROAD_Y = 0

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("lol")

all_sprites = pygame.sprite.Group()

# Drawing the window
def draw_window(egg_displacement = 0):
    screen.fill(WHITE)
    bg.draw_bg()
    draw_and_update_sprite()
    update_and_draw_egg(egg_displacement)
    pygame.display.update()
    

def update_and_draw_egg(egg_displacement):
    # TODO: Debug whatever this is: workaround- added a buffer length
    buffer = 28
    if(egg.rect.x + egg_displacement < ROAD_X - buffer):
        return
    if(egg.rect.x + egg.width + egg_displacement >= ROAD_X + ROAD_WIDTH + buffer):
        return
    egg.update_position(egg.rect.x + egg_displacement)
    egg.draw_egg(egg_displacement)



def draw_and_update_sprite():
    all_sprites.update()
    # update the sprites
    all_sprites.draw(screen)

def calculate_egg_displacement(VELOCITY, keys):
    if keys[pygame.K_LEFT]:
        egg_displacement = -VELOCITY
    elif keys[pygame.K_RIGHT]:
        egg_displacement = VELOCITY
    else:
        egg_displacement = 0
    return egg_displacement

# Create the road sprite
def create_road(GREY, BLACK, HEIGHT, ROAD_WIDTH, ROAD_X, ROAD_Y, all_sprites):
    road_sprite = Road(ROAD_X, ROAD_Y, ROAD_WIDTH, HEIGHT, GREY, BLACK)
    all_sprites.add(road_sprite)

# Main loop
running = True
clock = pygame.time.Clock()
run =  True
create_road(GREY, BLACK, HEIGHT, ROAD_WIDTH, ROAD_X, ROAD_Y, all_sprites)
print("Starting game....", screen)
egg = Egg(screen, 250)
bg = Background(screen, WIDTH + 20, HEIGHT)
# Game loop
while running:
    # Event handling
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key pressed
    keys = pygame.key.get_pressed()
    egg_displacement = calculate_egg_displacement(VELOCITY, keys)    
         
    # Update game logic
    draw_window(egg_displacement)

    

# Quit Pygame
pygame.quit()