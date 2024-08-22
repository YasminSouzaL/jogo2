from enum import Enum
import os
import pygame
from classes.Deck import Deck
from classes.Card import Card
from classes.Rodadas import Rodadas
from classes.Rodada_pc import RodadasPC
from stylos import stylo

pygame.init()

class GameState(Enum):
    PLAYER_CREATION = 1
    PLAYER_VS_COMPUTER = 2
    RODADAS = 3
    RODADAS_PC = 4

class ScreenCard:
    '''
    Classe ScreenCard responsável por gerar e gerenciar as cartas para os jogadores.

    Ela tem dois estados possíveis:
    - Gerar cartas para 2 jogadores
    - Gerar cartas para 1 jogador
    '''

    def __init__(self, player_names, screen, state: GameState , difficulty):
        self.screen = screen
        self.running = True
        self.deck = Deck()
        self.player_cards = {}
        self.cards_drawn = False
        self.card_width = 80
        self.card_height = 120
        self.card_images = self.load_card_images()
        self.player_names = player_names
        self.state = state
        self.cardnow = None
        self.difficulty = difficulty
       
    def check_player(self):
        if self.state == 1:
            print("Jogadores:", self.player_names)
            if len(self.player_names) >= 2:
                self.deck.shuffle()
                self.player_cards = self.generate_player_cards()
                print("Cartas geradas para os jogadores:", self.player_cards)
                return True
            else:
                print("Não há jogadores suficientes.")
                return False
        elif self.state == 2:
            print("Jogadores:", self.player_names)
            if len(self.player_names) == 1:
                self.deck.shuffle()
                self.player_cards = self.generate_player_cards()
                print("Cartas geradas para os jogadores:", self.player_cards)
                return True
            else:
                print("Não há jogadores suficientes.")
                return False

    def generate_player_cards(self):
        player_cards = {}
        for player in self.player_names:
            player_cards[player] = self.deck.deal_hand(3)
        return player_cards

    def load_card_images(self):
        pygame.init()
        suits = ['Copas', 'Espadas', 'Paus', 'Ouro']
        values = ['4', '5', '6', '7', 'Q', 'J', 'K', 'As', '2', '3']
        base_path = "data/imagem/card"
        card_images = {}
        for suit in suits:
            for value in values:
                card_name = f"{value}_{suit}.png"
                card_path = os.path.join(base_path, card_name)
                if os.path.exists(card_path):
                    try:
                        card_image = pygame.image.load(card_path)
                        card_image = pygame.transform.scale(card_image, (self.card_width, self.card_height))
                        card_images[f"{value}_{suit}"] = card_image
                    except pygame.error as e:
                        print(f"Erro ao carregar a imagem: {card_path}. Erro: {e}")
                else:
                    print(f"Arquivo não encontrado: {card_path}")
        return card_images

    def run(self):
        print("Running Generatorcards")
        while self.running:
            if self.state == 1:
                if self.check_player():
                    self.cardnow = self.generate_player_cards
                    self.state = GameState.RODADAS
                    self.rounds = Rodadas(self.player_names, self.player_cards, self.card_images, self.cardnow,self.difficulty, 800, 600)
                    self.rounds.run()
                    break
                
            elif self.state == 2:
                if self.check_player():
                    self.state = GameState.RODADAS_PC
                    self.round2 = RodadasPC(self.player_names, self.player_cards, self.card_images,self.cardnow,self.difficulty,800, 600)
                    self.round2.run()
                    break
            else:
                print("Estado inválido!")
                self.running = False
                break

