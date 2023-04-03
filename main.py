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
    draw_and_update_sprite()
    update_and_draw_egg(egg_displacement)
    pygame.display.update()
    

def update_and_draw_egg(egg_displacement):
    # TODO: Debug whatever this is: workaround- added a buffer length
    buffer = egg.width / 2 + 10
    print (egg.x, " : ", egg_displacement, " : ",  egg.x + egg_displacement)
    if(egg.x + egg_displacement < ROAD_X - buffer):
        return
    if(egg.x + egg_displacement >= ROAD_X + ROAD_WIDTH - buffer):
        return
    egg.update_position(egg.x + egg_displacement)
    egg.draw_egg(egg_displacement)

# create the road sprite
road_sprite = Road(ROAD_X, ROAD_Y, ROAD_WIDTH, HEIGHT, GREY, BLACK)

all_sprites.add(road_sprite)

def draw_and_update_sprite():
    all_sprites.update()
    # update the sprites
    all_sprites.draw(screen)

running = True
clock = pygame.time.Clock()
run =  True
print("Starting game", screen)
egg = Egg(screen, 250)
# Game loop
while running:
    # Event handling
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Write code to get the key pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        egg_displacement = -VELOCITY
    elif keys[pygame.K_RIGHT]:
        egg_displacement = VELOCITY
    else:
        egg_displacement = 0    
    
         
    # Update game logic
    draw_window(egg_displacement)

    

# Quit Pygame
pygame.quit()