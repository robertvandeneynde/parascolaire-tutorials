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
    glClearColor(0.9, 0.9, 0.5, 1.0) # du jaune, 1.0 est la transparence
    glClear(GL_COLOR_BUFFER_BIT)
    
    glUseProgram(shader_program)
    
    glBindVertexArray(vertex_array_object)
    # ici on fera un dessin opengl utilisant le vao et le shader program
    glBindVertexArray(0)
    
    glUseProgram(0)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
