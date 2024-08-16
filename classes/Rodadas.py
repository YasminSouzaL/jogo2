import sys
import os 
import pygame
from classes.Hand import Hand
from classes.Pontuacao import Pontuacao
from stylos import stylo

class Rodadas:
    def __init__(self,player_names, player_cards, card_images, cardsnow, width, height):
        self.hand = Hand()
        self.running = True
        self.player_names = player_names
        self.player_cards = player_cards
        self.card_images = card_images
        self.cardsnow = cardsnow
        self.current_round = 1
        self.selected_cards = {}
        self.round_cards = []
        self.card_width = 170
        self.card_height = 140
        self.current_player_index = 0
        self.round_winners = []
        self.winner = None
        self.truco_called = False
        self.pontuacao = None
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_Title(self):
        title = stylo.TextTitle("Rodadas", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, 330, 80)
        title.draw(self.screen)

    def draw_text(self):
        text = stylo.TextTitle("Vez de ", stylo.Fonts.BUTTON_FONT, stylo.Colors.BLACK, 380, 130)
        text.draw(self.screen)


    def draw_background(self):
        background = pygame.image.load("data/imagem/background.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))

    def draw_cards(self):
        #Desenhar as cartas de cada jogador na tela
        x = 100
        y = 200
        for player, cards in self.player_cards.items():
            for card in cards:
                card_image = self.card_images[card]
                card_rect = card_image.get_rect(center=(x, y))
                self.screen.blit(card_image, card_rect)
                self.round_cards.append((card_rect, card))
                x += 200
            x = 100
            y += 200

    def draw_handleTruco(self):
        truco_button = stylo.TextBox(100, 50)
        truco_button_rect = truco_button.draw(self.screen, (330, 500))
        truco_text = stylo.Text("Truco", stylo.Fonts.BUTTON_FONT, stylo.Colors.BLACK, 330, 500)
        truco_text.draw(self.screen)
        return truco_button_rect
    
    def hand_winner(self, card1, card2):
        hand = Hand()  
        hand.add_card(card1)
        hand.add_card(card2)
        print(f"Vencedor da rodada: {hand.winner()}")

    def check_round_winner(self):
        if len(self.selected_cards) == len(self.player_names):
            print(f"Cartas jogadas na rodada: {self.selected_cards}")
            winning_card = None
            round_winner = None
            for player, card in self.selected_cards.items():
                if winning_card is None or card.value > winning_card.value:
                    winning_card = card
                    round_winner = player
            self.round_winners.append(round_winner)
            print(f"Ganhador da rodada: {round_winner}")
    

    def draw(self):
        self.screen.fill(stylo.Colors.WHITE)
        self.draw_Title()
        self.draw_text()
        self.draw_cards()
        self.draw_handleTruco()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for card_rect, card in self.round_cards:
                        if card_rect.collidepoint(event.pos):
                            if card not in self.selected_cards.values():
                                self.selected_cards[self.current_player_index] = card
                                self.current_player_index = (self.current_player_index + 1) % len(self.player_names)
                                if len(self.selected_cards) == len(self.player_names):
                                    self.running = False
            pygame.display.flip()
        print("Cartas selecionadas:", self.selected_cards)
        return self.selected_cards


