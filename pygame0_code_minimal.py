#!coding: utf-8
from __future__ import print_function, division

from OpenGL.GL import *
from OpenGL.GL import shaders

import pygame
pygame.init()

taille = [512, 512]
ecran = pygame.display.set_mode(taille, pygame.OPENGL | pygame.DOUBLEBUF)

NOIR = [0, 0, 0]
BLANC = [1, 1, 1]
ROUGE = [1, 0, 0]
VERT = [0, 1, 0]
BLEU = [0, 0, 1]
ORANGE = [255/255, 153/255, 0]
ROSE = [1.0, 0.75, 0.80]

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
