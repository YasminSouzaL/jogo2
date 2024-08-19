'''
    Esta tela tem a classe de inimigo que é o computador e a classe de jogador (Player)

'''


import os
import pygame
from classes.Deck import Deck
from classes.Card import Card
from classes.Rodadas import Rodadas
from stylos import stylo

pygame.init()

class Rodadas_pc:
    def __init__(self,player_names, player_cards, card_images, cards_now_call_back, width, height):
        print()

