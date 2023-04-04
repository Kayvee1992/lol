import random
from background import Background
import pygame
from egg import *
from road import Road
from car import Car
from util import *
pygame.font.init()

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
CAR_WIDTH = 50
CAR_HEIGHT = 80

# Fonts


# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("lol")

all_sprites = pygame.sprite.Group()

# Drawing the window
def draw_window(egg_displacement = 0, crashed = False):
    screen.fill(WHITE)
    bg.draw_bg()
    draw_and_update_sprite()
    update_and_draw_egg(egg_displacement, crashed)
    draw_cars()
    pygame.display.update()
    
# Code to update the cars
def draw_cars():
    for car in cars:
        car.draw_car()

def update_and_draw_egg(egg_displacement, crashed):
    buffer = 0
    if (crashed):
        egg.draw_broken_egg(egg_displacement)
        return
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

def get_random_number():
    return random.randint(1, 5) 

def get_random_road_position():
    return random.randint(200, 350)


def handle_cars():
    create_car(get_random_road_position(), -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT, get_random_color())
    update_cars()


def update_cars():
    for car in cars:
        car.update()
        if car.rect.y > HEIGHT + CAR_HEIGHT:
            cars.remove(car)

def create_car(x, y, width, height, color):
    if (get_random_number() % 2 == 0 and len(cars) < 3):
        if(len(cars) > 1 and cars[len(cars)-1].rect.y < 100):
            return
        print("Creating car")
        car = Car(screen, x, y, width, height, color)
        cars.append(car)

def detect_collision():
    for car in cars:
        if (egg.rect.colliderect(car.rect)):
            print("Collision detected")
            return True 

# Main loop
running = True
clock = pygame.time.Clock()
run =  True
create_road(GREY, BLACK, HEIGHT, ROAD_WIDTH, ROAD_X, ROAD_Y, all_sprites)
print("Starting game....", screen)
egg = Egg(screen, 250)
bg = Background(screen, WIDTH + 20, HEIGHT)
cars = []
# Game loop
while running:
    # Event handling
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    # Key pressed
    keys = pygame.key.get_pressed()
    egg_displacement = calculate_egg_displacement(VELOCITY, keys)    
         
    handle_cars()
    crashed = False
    if detect_collision():
        running = False
        crashed = True
    draw_window(egg_displacement, crashed)
    if crashed:
        print("Game Over")
        pygame.time.delay(3000)
    
# Quit Pygame
pygame.quit()