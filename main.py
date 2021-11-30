import pygame, sys
from settings import *
from level import Level
import colores
import constantes

#Iniciamos el juego
pygame.init()
#tamaño da ventana
screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(level_map, screen)

#Bucle principal del juego
while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()
  screen.fill(colores.blanco)
  level.run()

  pygame.display.update()
  clock.tick(constantes.FPS)

