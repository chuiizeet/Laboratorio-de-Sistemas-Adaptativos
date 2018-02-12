#Problema!
import math
import random
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(1500)]

#Colores RGB
Colores = [[255,87,51],[88,255,51],[243,0,255],[255, 102, 255],[204, 0, 102],[255, 255, 0],[0, 204, 0],[153, 0, 255],[0, 51, 0],[51, 51, 204],
[255,87,51],[88,255,51],[243,0,255],[255, 102, 255],[204, 0, 102],[255, 255, 0],[0, 204, 0],[153, 0, 255],[0, 51, 0],[51, 51, 204],
[255,87,51],[88,255,51],[243,0,255],[255, 102, 255],[204, 0, 102],[255, 255, 0],[0, 204, 0],[153, 0, 255],[0, 51, 0],[51, 51, 204]]

#Funcion explotar
def explotar(n,posx,posy,rad):
    for i in range(rad):
        screen.fill((0,0,0))
        for speed, angle in particles:
            distance = i * speed
            x = posx + distance * math.cos(angle)
            y = posy + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (Colores[n])) #Color
        pygame.display.flip()

def explosiones2():
    numExp = 12
    coordx = 0
    coordy = 400
    radio = 50
    Color = 255, 102, 255
    for i in range(numExp):
        coordx += 50
        explotar2(coordx,coordy,radio,Color)

def explotar2(cx, cy, r, c):
	for i in range(r):
		screen.fill((0,0,0))
		for speed, angle in particles:
			distance = i * speed
			x = cx + distance * math.cos(angle)
			y = cy + distance * math.sin(angle)
			screen.set_at((int(x), int(y)), c)
		pygame.display.flip()


#Funcion Secuencia_explociones
def secuencia_explociones(n):
    for x in range(0,n):
        posx = random.randint(1,400)
        posy = random.randint(1,400)
        rad = random.randint(1,399)
        #Coordenadas
        print("\n")
        print("La coordenada en x de la explosion ", x, "es:", posx)
        print("La coordenada en y de la explosion ", x, "es:", posy)
        print("El radio de la explosion ", x, "es:", rad)
        print("=======================================================\n")
        explotar(x,posx,posy,rad)

#funcion secuencia explosiones linea recta
def secuencia_explociones_linea():
    y = 100
    c = 0
    x = 0
    rad = 399
    for y in range(0,400):
        y += 100
        c += 1
        explotar(c,x,y,rad)


#Main
def main():
    if len(sys.argv) == 1:
        print("Explosiones random")
        secuencia_explociones(12)
        explosiones2()
    else:
        secuencia_explociones(int(sys.argv[1]))
        explosiones2()

main()
