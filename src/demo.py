import pygame

# initialize Pygame
pygame.init()

# set up the game window
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rectangle with border")

# define the rectangle
rect_width = 100
rect_height = 50
rect_x = 100
rect_y = 100
rect_color = (255, 0, 0)
border_color = (0, 0, 255)
border_width = 3

# set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background
    window.fill((255, 255, 255))

    # draw the rectangle
    pygame.draw.rect(window, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(window, border_color, (rect_x, rect_y, rect_width, rect_height), border_width)

    # update the screen
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

# quit Pygame
pygame.quit()
