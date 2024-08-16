
import os
import sys
import pygame
from classes.Deck import Deck
from classes.Card import Card
from classes.Rodadas import Rodadas
from stylos import stylo

pygame.init()

class ScreenCard:
    '''
        Classe ScreenCard responsive por gerar e gerenciar as cartas para os jogadores.
    '''

    def __init__(self,player_names):
        self.running = True
        self.deck = Deck()
        self.player_cards = {}
        self.cards_drawn = False
        self.card_width = 80
        self.card_height = 120
        self.card_images = self.load_card_images()
        self.player_names = player_names

    def check_player(self):
        print("Jogadores:", self.player_names)
        if len(self.player_names) >= 2:
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
    
    #Ir para a próxima Classe rodada
    def run(self):
        print("Running Generatorcards")
        while self.running:
            if self.check_player():
                #receber cartas novas do metodo generate_player_cards
                self.cardsnow =  self.generate_player_cards()
                self.rounds = Rodadas(self.player_names, self.player_cards, self.card_images,self.cardsnow, 800,600)
                self.rounds.run()
                break
            else:
                self.running = False
                break
        return self.player_cards


    '''
        Main - Start the game (player_creation_screen = PlayerCreationScreen(800, 600)  
            player_creation_screen.run())
        PlayerCreationScreen - Generatorcards (player_creation_screen.players)
        Generatorcards - Rodadas (800,600,player_creation_screen.players, mao.load_card_images)
    '''