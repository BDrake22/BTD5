'''
Created on Jul 31, 2021

@author: braydendrake
'''

import pygame
import time
import math
time0 = time.time()
pygame.init()
monkeys= []
bloonsX = []
bloonsY = []
bloonsY = []
screen = pygame.display.set_mode((600,400))

pygame.display.set_caption("Brayden's BTD69")
icon = pygame.image.load("tower.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("background.png")
bloon = pygame.image.load("balloon.png")
monkey = pygame.image.load("Btd6monkey.png")
running = True
round=1
cash = 1000
font = pygame.font.Font('freesansbold.ttf', 24)

textX = 10
textY = 10
livesX = 10
livesY = 40
lives = 50

# class RedBloon(object):
#     """docstring for RedBloon."""
#
#     def __init__(self, health, speed, reward):
#         self.health = 1
#         self.speed = 1
#         self.reward = 1
#



for i in range(round*10):
    bloonsX.append(0)
    bloonsY.append(210)
def show_score(x, y):
    temp_score = font.render("Cash : $" + str(cash), True, (255,255,0))
    screen.blit(temp_score, (x, y))
def show_lives(x, y):
    temp_score = font.render("Lives : " + str(lives), True, (255,0,0))
    screen.blit(temp_score, (x, y))

dartImg = pygame.image.load("dart.jpg")
dartX = 0
dartY = 0
dartX_change = 1
dartY_change = 1
dart_state = "ready"

def fire_dart(x,y):
    global dart_state
    dart_state = "fire"
    screen.blit(dartImg, (x, y))

    print("fire")


def balloon(round):
    # bloonlist(round)
    # print(bloonsX)
    # print(bloonsY)
    realtime = time0 - time.time()
    print(int(realtime))
    i = abs(int(realtime) / 3)
    for j in range(int(i)):
        screen.blit(bloon, (bloonsX[j], bloonsY[j]))
        if (bloonsX[j] < 92) and (bloonsY[j] > 100):
            bloonsX[j] += 2
        elif (bloonsX[j] > 92) and (bloonsY[j] > 100) and (bloonsX[j] <150):
            bloonsY[j] -= 2
        elif (bloonsX[j] < 210) and (bloonsY[j] < 100):
            bloonsX[j] += 2
        elif (bloonsX[j] > 210) and (bloonsY[j] >= 96) and (bloonsY[j] < 250) and (bloonsX[j] < 370):
            bloonsY[j] += 2
        elif (bloonsX[j] > 210) and (bloonsY[j] >= 254) and (bloonsX[j] < 370):
            bloonsX[j] += 2
        elif (bloonsX[j] > 375) and (bloonsY[j] <= 254) and (bloonsY[j]>180):
            bloonsY[j] -= 2
        elif (bloonsX[j] > 375) and (bloonsY[j] <= 180):
            bloonsX[j] += 2
        else:
            bloonsX[j] += 2
def bloonlist(round):
    # print("made it")
    # bloonsX = []
    # bloonsY = []
    curr_round = round *10
    for i in range(curr_round):
        bloonsX.append(0)
        bloonsY.append(270)
def towers():
    i=0
    while i < len(monkeys):
        screen.blit(monkey, (monkeys[i],monkeys[i+1]))
        i+=2
def check_enemy_distance():
    i = 0
    while i < len(monkeys):
        j = 0
        while j < len(bloonsX):
            distance = math.sqrt(math.pow(bloonsX[j] - monkeys[i], 2) + math.pow(bloonsY[j] - monkeys[i+1],2))
            if distance < 70:
                return True, bloonsX[j], bloonsY[j]
            else:
                j += 1
                continue
        i+=2
    return False, 0, 0
while running:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            monkeys.append(mouse_x - 15)
            monkeys.append(mouse_y - 15)

    # screen.fill(255,0,0)
    towers()
    balloon(round)
    in_distance, bx, by = check_enemy_distance()
    if in_distance:
        fire_dart(bx, by)
    show_score(textX, textY)
    show_lives(livesX, livesY)
    pygame.display.update()
