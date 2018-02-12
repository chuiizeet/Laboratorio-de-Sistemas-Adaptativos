<<<<<<< HEAD
#Problema!
import math
import random
import pygame
import sys
=======
import math
import random
import pygame
>>>>>>> master

pygame.init()

screen = pygame.display.set_mode((800, 800))
<<<<<<< HEAD
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(1500)]
#(random.gauss(0,.5), random.uniform(0,6.28318))


def explotar():
    for i in range(399):
        screen.fill((0,0,0))
        for speed, angle in particles:
            distance = i * speed
            x = 400 + distance * math.cos(angle)
            y = 400 + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (200,0,0)) #Color
        pygame.display.flip()

def secuencia_explociones(n):
    for x in range(0,n):
        explotar()

secuencia_explociones(2)
=======
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(2000)]

for i in range(399):
    screen.fill((255,255,255))
    for speed, angle in particles:
        distance = i * speed
        x = 400 + distance * math.cos(angle)
        y = 400 + distance * math.sin(angle)
        screen.set_at((int(x), int(y)), (0,0,0))
    pygame.display.flip()
>>>>>>> master
