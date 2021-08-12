import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((300, 200))



pygame.display.update()
clock = pygame.time.Clock()
finished = False
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()