import pygame
from pygame.draw import *
import sys

pygame.init()

FPS = 50
screen = pygame.display.set_mode((400, 400))
# face
circle(screen, (223, 213, 165), (200, 200), 150, 0)
# mouth
rect(screen, (0, 0, 0), (100, 250, 200, 30))
# eyes (left, right)
circle(screen, (255, 0, 0), (150, 140), 20, 0)
circle(screen, (255, 0, 0), (250, 140), 20, 0)
# eyebrows (left, right)
line(screen, (150, 75, 0), (30, 60), (190, 120), 15)
line(screen, (150, 75, 0), (270, 60), (220, 120), 15)
# eye dots (left, right)
circle(screen, (0, 0, 0), (150, 140), 4, 0)
circle(screen, (0, 0, 0), (250, 140), 4, 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
