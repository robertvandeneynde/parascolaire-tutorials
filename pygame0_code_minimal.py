#!coding: utf-8
from __future__ import print_function, division

from OpenGL.GL import *
from OpenGL.GL import shaders

from vec3_utils import *

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

vertex_shader = '''
#version 330
// vertex shader

in vec4 position; // on lit le xyzw

void main() {
    gl_Position = position; // et on l'écrit
}
'''

fragment_shader = '''
#version 330
// fragment shader

out vec4 pixel; // notre but est de donner la couleur du pixel

void main() {
    pixel = vec4(1, 0.5, 0, 1); // orange, transparence 100%
}
'''

shader_program = shaders.compileProgram(
    shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

vertices = farray([
    0.6, 0.6, 0.0, 1.0,
    -0.6, 0.6, 0.0, 1.0,
    0.0, -0.6, 0.0, 1.0,
])

vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object) # on sélectionne le vao "vertex_array_object"

vertex_buffer = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer) # on sélectionne le vbo "vertex_buffer"
glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW)

position = glGetAttribLocation(shader_program, 'position')
if position != -1:
    glEnableVertexAttribArray(position) # on active l'attribut position
    glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0)) # données par groupe de 4 Float dans l'attribut position
else:
    print('inactive attribute "{}"'.format('position'))

glBindBuffer(GL_ARRAY_BUFFER, 0) # aucun vbo sélectionné
glBindVertexArray(0) # aucun vao sélectionné

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
    glDrawArrays(GL_TRIANGLES, 0, 3) # on dessine 3 points, on commence au point numéro 0, on en fait des TRIANGLES
    glBindVertexArray(0)
    
    glUseProgram(0)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
