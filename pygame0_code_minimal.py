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

ma_position = 600
sens = 1

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    if sens == -1:
        ma_position = ma_position - 5
    else:
        ma_position = ma_position + 5
    if ma_position > 700:
        sens = -1
    if ma_position < 0:
        sens = 1
    print(sens, ma_position)

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    if sens == -1:
        pygame.draw.polygon(ecran, ROUGE, [
            [ma_position + 0 - 50, 80 + 50 - 50],
            [ma_position + 100 - 50, 80 + 0 - 50],
            [ma_position + 100 - 50, 80 + 100 - 50]])
    else:
        pygame.draw.polygon(ecran, ROUGE, [
            [ma_position + 100 - 50, 80 + 50 - 50],
            [ma_position + 0 - 50, 80 + 0 - 50],
            [ma_position + 0 - 50, 80 + 100 - 50]])
    pygame.draw.circle(ecran, VERT, [ma_position, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
