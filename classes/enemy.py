'''
    Criar ideia da maquina jogar com base em um algoritmo de decisão
    O computador tem duas Fases : Uma aleatoria e uma que ele tentar sempre ganhar a 1 rodada 
    Isso é definida pelo nilve de dificuldade tipo medio(1), dificil(2)

'''

import pygame
import random

class Enemy:
    def __init__(self, player_cards, difficulty):
        self.player_cards = player_cards  # Cartas do computador
        self.difficulty = difficulty      # Dificuldade: 1 (Médio), 2 (Difícil)
        self.selected_card = None         # Carta escolhida pelo inimigo
        self.first_round = True           # Controla se é a primeira rodada

    def play(self):
        if not self.player_cards:  # Verifica se a lista não está vazia
            raise ValueError("Nenhuma carta disponível para jogar.")
            self.selected_card = random.choice(self.player_cards)
            return self.selected_card

        if self.difficulty == 1:
            self.selected_card = random.choice(self.player_cards)
        elif self.difficulty == 2:
            if self.first_round:
                self.selected_card = self.play_to_win()
                self.first_round = False  # Após a primeira rodada, marcar como jogada
            else:
                self.selected_card = random.choice(self.player_cards)
        return self.selected_card


    def play_to_win(self):
        """
        No nível difícil, tenta escolher a carta que tenha a maior chance de ganhar.
        Este método é chamado apenas na primeira rodada.
        """
        # Cria um dicionário com as cartas e suas probabilidades de ganhar
        cards_prob = {}
        for card in self.player_cards:
            cards_prob[card] = self.calculate_win_probability(card)
        # Escolhe a carta com a maior probabilidade
        return max(cards_prob, key=cards_prob.get)


    
    