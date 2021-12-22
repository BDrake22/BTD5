'''
Created on Jul 31, 2021

@author: braydendrake
'''

import pygame
import time
import math
import random

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Brayden's Blackjack")
bg = pygame.image.load("table.png")
running = True
while running:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
