import pygame
from pygame.draw import *
from functions import clouds, house, tree


pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 400))

# background
rect(screen, (167, 176, 202), (0, 0, 600, 200))
rect(screen, (129, 174, 157), (0, 200, 600, 400))
# from functions.py
clouds(180, 80, screen)
clouds(400, 100, screen)
house(150, 160, screen)
tree(80, 190, screen)
tree(450, 210, screen)

clock = pygame.time.Clock()
pygame.display.update()
finished = False
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
