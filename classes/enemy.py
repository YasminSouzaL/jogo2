'''
    Criar ideia da maquina jogar com base em um algoritmo de decisão
    Criar a classe Enemy
    Criar a classe Player
    Criar a classe Game

'''

#classe Enemy

import pygame
import random

class Enemy:
    '''
        Classe que representa o computador como jogador para 1 x computador
        ele vai direcionar a jogada do computador
    '''

    def __init__(self, player_cards):
        self.player_cards = player_cards
        self.selected_card = None
        self.selected_card = random.choice(self.player_cards)

    def play(self):
        '''
            Metodo que representa a jogada do computador
        '''
        self.selected_card = random.choice(self.player_cards)
        return self.selected_card
    
    def __str__(self):
        return f"Carta selecionada: {self.selected_card}"
    
    def __repr__(self):
        return self.__str__()