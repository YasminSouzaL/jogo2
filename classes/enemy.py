'''
    Criar ideia da maquina jogar com base em um algoritmo de decisão
    screen_card = ScreenCard(self.player_cards e self.difficulty)
    screen_card.run()
    O computador tem duas Fases : Uma aleatoria e uma que ele tentar sempre ganhar a 1 rodada 
    Isso é definida pelo nilve de dificuldade tipo medio(1), dificil(2)

'''

import os
import pygame
import random
from classes.Card import Card
from classes.Hand import Hand
from classes.Deck import Deck


class Enemy:
    # def __init__(self, difficulty):
    #     self.enemy = ['PC']
    #     self.difficulty = difficulty
    #     self.deck = Deck()  # Inicializa o baralho antes de gerar as cartas
    #     self.hand = Hand()
    #     self.enemy_card = self.generate_enemy_cards()  # Agora você pode gerar as cartas do inimigo
    
    #     print("Estou na classe Enemy")
    #     print("Dificuldade na classe Enemy:", self.difficulty)

    # def generate_enemy_cards(self):
    #     enemy_card = {}
    #     for enemy in self.enemy:
    #         enemy_card[enemy] = self.deck.deal_hand(3)
    #     return enemy_card

    # def load_card_images(self):
    #     pygame.init()
    #     suits = ['Copas', 'Espadas', 'Paus', 'Ouro']
    #     values = ['4', '5', '6', '7', 'Q', 'J', 'K', 'As', '2', '3']
    #     base_path = "data/imagem/card"
    #     card_images = {}
    #     for suit in suits:
    #         for value in values:
    #             card_name = f"{value}_{suit}.png"
    #             card_path = os.path.join(base_path, card_name)
    #             if os.path.exists(card_path):
    #                 try:
    #                     card_image = pygame.image.load(card_path)
    #                     card_image = pygame.transform.scale(card_image, (self.card_width, self.card_height))
    #                     card_images[f"{value}_{suit}"] = card_image
    #                 except pygame.error as e:
    #                     print(f"Erro ao carregar a imagem: {card_path}. Erro: {e}")
    #             else:
    #                 print(f"Arquivo não encontrado: {card_path}")
    #     return card_images

    # def play(self):
    #     if self.difficulty == 1:
    #         return self.play_random()
    #     elif self.difficulty == 2:
    #         return self.play_smart()
    #     else:
    #         raise ValueError("Dificuldade inválida.")

    def __init__(self, difficulty):
        self.enemy = ['PC']
        self.difficulty = difficulty
        self.deck = Deck()
        self.hand = Hand()
        self.enemy_card = self.generate_enemy_cards()
        print("Estou na classe Enemy")
        print("Dificuldade na classe Enemy:", self.difficulty)

    def generate_enemy_cards(self):
        enemy_card = {}
        for enemy in self.enemy:
            enemy_card[enemy] = self.deck.deal_hand(3)
        self.hand.cards = enemy_card[self.enemy[0]]  # Adiciona as cartas à mão do inimigo
        return enemy_card

    # def play(self):
    #     if len(self.hand.cards) == 0:
    #         print("O inimigo não tem cartas para jogar.")
    #         return None
        
    #     if self.difficulty == 1:
    #         card_to_play = self.play_random()
    #     elif self.difficulty == 2:
    #         card_to_play = self.play_smart()
    #     else:
    #         raise ValueError("Dificuldade inválida.")
        
    #     print(f"O inimigo jogou: {card_to_play}")
    #     self.hand.remove_card(card_to_play)
    #     return card_to_play
 
    def play(self):
        # Verifica se ainda há cartas na mão do inimigo
        if len(self.hand) == 0:
            print("O inimigo não tem mais cartas.")
            return None

        # Escolhe a primeira carta (ou pode implementar uma lógica de escolha mais complexa)
        card_to_play = self.hand.cards[0]

        # Remove a carta da mão
        self.hand.remove_card(card_to_play)

        print(f"O inimigo jogou: {card_to_play}")
        return card_to_play

    def play_random(self):
        return random.choice(self.hand.cards)
    
    def play_smart(self):
        return max(self.hand.cards)

    def play_random(self):
        if len(self.hand.cards) == 0:
            print("O inimigo não tem cartas para jogar.")
            return None 
        card_to_play = random.choice(self.hand.cards)
        if card_to_play in self.hand.cards:
            self.hand.remove_card(card_to_play)
        else:
            print(f"Carta {card_to_play} não encontrada na mão do inimigo.")
        return card_to_play
    

    def play_smart(self):
        if len(self.hand.cards) == 0:
            print("O inimigo não tem cartas para jogar.")
            return None
        card_to_play = max(self.hand.cards)
        self.hand.remove_card(card_to_play)
        return card_to_play

    def get_enemy(self):
        return self.enemy
    
    def set_enemy(self, enemy):
        self.enemy = enemy

    def get_enemy_card(self):
        return self.enemy_card
    
    def get_enemy_card_value(self):
        return self.enemy_card_value
    
    def get_enemy_card_suit(self):
        return self.enemy_card_suit
