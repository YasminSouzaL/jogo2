import os
import pygame
import random
from classes.Card import Card
from classes.Hand import Hand
from classes.Deck import Deck

class Enemy:
    def __init__(self, difficulty):
        self.enemy = ['PC']
        self.difficulty = difficulty
        self.deck = Deck()
        self.hand = Hand()
        self.enemy_card = self.generate_enemy_cards()
        self.current_round = 0  # Inicializa current_round
        print("Estou na classe Enemy")
        print("Dificuldade na classe Enemy:", self.difficulty)

    def generate_enemy_cards(self):
        enemy_card = {}
        for enemy in self.enemy:
            enemy_card[enemy] = self.deck.deal_hand(3)
        self.hand.cards = enemy_card[self.enemy[0]]  # Adiciona as cartas à mão do inimigo
        return enemy_card

    def play(self):
        if len(self.hand.cards) == 0:
            print("O inimigo não tem mais cartas.")
            return None

        if self.difficulty == 0:  # Fácil
            card_to_play = self.play_random()
        elif self.difficulty == 1:  # Médio
            card_to_play = self.play_smart() if self.current_round == 0 else self.play_random()
        else:  # Difícil
            card_to_play = self.play_smart()

        self.current_round += 1  # Incrementa a rodada após a jogada

        if card_to_play:
            print(f"O inimigo jogou: {card_to_play}")
        return card_to_play

    def play_random(self):
        if len(self.hand.cards) == 0:
            print("O inimigo não tem cartas para jogar.")
            return None 
        card_to_play = random.choice(self.hand.cards)
        self.hand.remove_card(card_to_play)
        return card_to_play
    
    def play_smart(self):
        if len(self.hand.cards) == 0:
            print("O inimigo não tem cartas para jogar.")
            return None
        card_to_play = max(self.hand.cards, key=lambda card: card.value)
        self.hand.remove_card(card_to_play)
        return card_to_play

    def get_enemy(self):
        return self.enemy
    
    def set_enemy(self, enemy):
        self.enemy = enemy

    def get_enemy_card(self):
        return self.enemy_card
