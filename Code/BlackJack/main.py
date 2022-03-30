'''
Created on Jul 31, 2021

@author: braydendrake
'''

import pygame
import time
import math
import random
suits = ['C', 'S', 'H', 'D']
new_player_card_pos = [550,450]
new_dealer_card_pos = [650,50]
cards_to_print = []
cards_pos = []
player_score = 0
dealer_score = 0
dealer_score_hidden = 0
player_ace = 0
dealer_ace = 0
blank_indicator = True
dealer_extra_cards = []
dealer_extra_cards_pos = []
new_game_question = False
def determine_card():
    global player_ace
    card = random.randint(1,13)
    score = card
    if card == 1:
        card = 'A'
        # player_ace += 1
        score = 11
    elif card > 10:
        if card == 11:
            card = 'J'
            score = 10
        elif card == 12:
            card = 'Q'
            score = 10
        elif card == 13:
            card = 'K'
            score = 10
    card = str(card) + suits[random.randint(0,3)] + '.png'
    return card, score
def start():
    global player_score
    global dealer_score
    global dealer_score_hidden
    global player_ace
    p1, score = determine_card()
    player_score += score
    if score == 11:
        player_ace+=1
    p2, score = determine_card()
    player_score += score
    if score == 11:
        player_ace+=1
    d1, score = determine_card()
    dealer_score += score
    d2, score = determine_card()
    dealer_score_hidden += score
    ready_for_new_hand = False
    p1 = pygame.image.load(p1)
    p1 = pygame.transform.scale(p1, (100,200))
    p2 = pygame.image.load(p2)
    p2 = pygame.transform.scale(p2, (100,200))
    d1 = pygame.image.load(d1)
    d1 = pygame.transform.scale(d1, (100,200))
    d2 = pygame.image.load(d2)
    d2 = pygame.transform.scale(d2, (100,200))
    cards_to_print.append(p1)
    cards_to_print.append(p2)
    cards_to_print.append(d1)
    # cards_to_print.append(d2)
    dealer_extra_cards.append(d2)
    cards_pos.append((450,550))
    cards_pos.append((500,500))
    cards_pos.append((550,50))
    dealer_extra_cards_pos.append((450,50))
    # cards_pos.append((450,50))
    return ready_for_new_hand
def print_cards():
    #print(cards_to_print)
    # print(cards_pos)
    if (player_ace > 0):
        print_score = font.render("Player: " + str(player_score-10) + '/' + str(player_score), True, (255,255,255))
    else:
        print_score = font.render("Player: " + str(player_score), True, (255,255,255))
    screen.blit(print_score, (500,770))
    for i in range(len(cards_to_print)):
        screen.blit(cards_to_print[i], cards_pos[i])

def cards():
    global blank
    if blank_indicator:
        blank = pygame.image.load("blank.png")
        blank = pygame.transform.scale(blank, (100,200))
        screen.blit(blank, (450,50))
    print_cards()
    # screen.blit(p1, (450,550))
    # screen.blit(p2, (500,500))
    # screen.blit(d1, (550,50))

def buttons():
    hit = pygame.image.load("hit.png")
    hit = pygame.transform.scale(hit, (75,75))
    screen.blit(hit, (900, 700))
    stand = pygame.image.load("stand.png")
    stand = pygame.transform.scale(stand, (75,75))
    screen.blit(stand, (975, 700))
    double = pygame.image.load("double_down.png")
    double = pygame.transform.scale(double, (75,75))
    screen.blit(double, (1050, 700))

def check_mouse(x,y):
    global new_game_question
    if new_game_question == True:
        print(f"x == {x}, y == {y}")
        if (x >= 1100) and (x <1175) and (y <= 475) and (y >= 400):
            print("made it")
            decision = 'start new game'
            return decision
    else:
        if (x >= 900) and (x <975) and (y >= 700):
            decision = 'hit'
        elif (x >= 975) and (x <1050) and (y >= 700):
            decision = 'stand'
        elif (x >= 1050) and (x <1200) and (y >= 700):
            decision = 'double'
        else:
            decision = 'na'
        return decision

def add_card(card):
    print(card)
    card = pygame.image.load(card)
    card = pygame.transform.scale(card, (100,200))
    cards_to_print.append(card)
    cards_pos.append(new_player_card_pos.copy())
    new_player_card_pos[0] += 50
    new_player_card_pos[1] -= 50


def new_card(action):
    global player_ace
    global player_score
    if action == 'hit':
        card, score = determine_card()
        if score == 11:
            player_ace+=1
        player_score += score
        add_card(card)
        return 'na'
    elif action == 'stand':
        dealer_turn()
def dealer_turn():
    global dealer_score
    global dealer_score_hidden
    global blank_indicator
    global player_ace
    player_ace = 0
    dealer_score += dealer_score_hidden
    blank_indicator = False

def ask_to_play_again():
    again = font.render("Deal Again?", True, (255,255,255))
    screen.blit(again, (540,300))
    new_game_button = pygame.image.load("play_again.png")
    new_game_button = pygame.transform.scale(new_game_button, (75,75))
    screen.blit(new_game_button, (1100, 400))

def dealer_turn_finish():
    global dealer_score
    global dealer_extra_cards_pos
    global player_score
    global dealer_ace
    global new_game_question
    for i in range(len(dealer_extra_cards)):
        screen.blit(dealer_extra_cards[i], dealer_extra_cards_pos[i])
    if dealer_score > 21:
        if dealer_ace > 0:
            dealer_ace = 0
            dealer_score -= 10
        winner = font.render("You Win", True, (255,255,255))
        screen.blit(winner, (540,350))
        new_game_question = True
    elif dealer_score < 17:
        card, score = determine_card()
        if score == 11:
            dealer_ace+=1
        dealer_score += score
        d_ex = pygame.image.load(card)
        d_ex = pygame.transform.scale(d_ex, (100,200))
        dealer_extra_cards.append(d_ex)
        dealer_extra_cards_pos.append(new_dealer_card_pos.copy())
        new_dealer_card_pos[0] += 100
        print(card)
    else:
        if dealer_score > player_score:
            loser = font.render("You lose", True, (255,255,255))
            screen.blit(loser, (540,350))
            new_game_question = True
        elif dealer_score < player_score:
            winner = font.render("You Win", True, (255,255,255))
            screen.blit(winner, (540,350))
            new_game_question = True
        else:
            push = font.render("Push", True, (255,255,255))
            screen.blit(push, (540,350))
            new_game_question = True

def dealer_score_print():
    global dealer_score
    global dealer_score_hidden
    print_score = font.render("Dealer: " + str(dealer_score), True, (255,255,255))
    screen.blit(print_score, (500,10))
def check_win():
    global new_game_question
    global player_score
    global player_ace
    if player_score == 21:
        player_ace = 0
        winner = font.render("You Win", True, (255,255,255))
        screen.blit(winner, (540,350))
        new_game_question = True
    elif player_score > 21:
        if player_ace > 0:
            player_ace = 0
            player_score -= 10
        else:
            loser = font.render("Bust", True, (255,255,255))
            screen.blit(loser, (540,350))
            new_game_question = True
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Brayden's Blackjack")
bg = pygame.image.load("table.png")
font = pygame.font.Font('freesansbold.ttf', 24)
running = True
ready_for_new_hand = True
action = 'na'
while running:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            action = check_mouse(mouse_x, mouse_y)
            print(action)
        if action != 'na':
            action = new_card(action)
    if ready_for_new_hand == True:
        ready_for_new_hand = start()
    # print(player_card_1, player_card_2, dealer_card_1, dealer_card_2)
    cards()
    buttons()
    check_win()
    dealer_score_print()
    if new_game_question:
        ask_to_play_again()
    if blank_indicator == False:
        dealer_turn_finish()
    pygame.display.update()
