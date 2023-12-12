import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 800
BACKGROUND_COLOR = (0, 0, 0)
RECTANGLE_COLOR = (255, 0, 0)
RECTANGLE_WIDTH, RECTANGLE_HEIGHT = 50, 50
RECTANGLE_SPEED = 5


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")

x, y = (WIDTH - RECTANGLE_WIDTH) // 2, (HEIGHT - RECTANGLE_HEIGHT) // 2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= RECTANGLE_SPEED
    if keys[pygame.K_DOWN]:
        y += RECTANGLE_SPEED
    if keys[pygame.K_LEFT]:
        x -= RECTANGLE_SPEED
    if keys[pygame.K_RIGHT]:
        x += RECTANGLE_SPEED

  
    screen.fill(BACKGROUND_COLOR)


    pygame.draw.rect(screen, RECTANGLE_COLOR, (x, y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT))

    pygame.display.update()

  
    clock.tick(60)


pygame.quit()
sys.exit()
