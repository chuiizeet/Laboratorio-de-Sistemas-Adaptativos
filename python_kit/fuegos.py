import math
import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(2000)]

for i in range(399):
    screen.fill((255,255,255))
    for speed, angle in particles:
        distance = i * speed
        x = 400 + distance * math.cos(angle)
        y = 400 + distance * math.sin(angle)
        screen.set_at((int(x), int(y)), (0,0,0))
    pygame.display.flip()