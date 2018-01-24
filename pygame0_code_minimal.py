#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT

mon_x = 600
mon_y = 80
sens = 1

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    if sens == -1:
        mon_x = mon_x - 5
    else:
        mon_x = mon_x + 5
    if mon_x > 700:
        sens = -1
    if mon_x < 0:
        sens = 1
    print(sens, mon_x)

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    
    centre_triangle_x, centre_triangle_y = 50, 50
    
    if sens == -1:
        pygame.draw.polygon(ecran, ROUGE, [
            [mon_x + 0 - centre_triangle_x, mon_y + 50 - centre_triangle_y],
            [mon_x + 100 - centre_triangle_x, mon_y + 0 - centre_triangle_y],
            [mon_x + 100 - centre_triangle_x, mon_y + 100 - centre_triangle_y]])
    else:
        pygame.draw.polygon(ecran, ROUGE, [
            [mon_x + 100 - centre_triangle_x, mon_y + 50 - centre_triangle_y],
            [mon_x + 0 - centre_triangle_x, mon_y + 0 - centre_triangle_y],
            [mon_x + 0 - centre_triangle_x, mon_y + 100 - centre_triangle_y]])
    
    pygame.draw.circle(ecran, VERT, [mon_x, mon_y], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
