'''
    Esta tela tem a classe de inimigo que é o computador e a classe de jogador (Player)

'''


import os
import pygame
from classes.Deck import Deck
from classes.Card import Card
from classes.Hand import Hand
from classes.Pontuacao import Pontuacao
from classes.enemy import Enemy
from stylos import stylo

pygame.init()

class RodadasPC:
    def __init__(self, player_names, player_cards, card_images, cards_now_call_back, difficulty, width, height):
        self.player_names = player_names
        self.player_cards = player_cards
        self.card_images = card_images
        self.cardsnow = cards_now_call_back
        self.width = width
        self.height = height
        self.deck = Deck()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.difficulty = difficulty
        self.enemy = Enemy(self.player_cards,self.difficulty)  # Cria a instância de Enemy
        print("A dificuldade é:", self.difficulty)
        print("Estou na tela RODADAPC")

    def draw_Title(self):
        title = stylo.TextTitle("Rodadas com PC", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 7)
        title.draw(self.screen)

    def draw_Text(self):
        text = stylo.Text("Vez de: " + self.player_names[0], stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, self.width // 2, self.height // 3)
        text.draw(self.screen)


    '''
        def draw_Card(self, player):
        x = 150
        y = 350
        for card in self.player_cards[player]:
            card_image = self.card_images[f"{card.value}_{card.suit}"]
            card_rect = card_image.get_rect()
            card_rect.topleft = (x, y)
            self.screen.blit(card_image, card_rect)
            self.round_cards.append((card_rect, card))
            x += 200
    '''

    def draw_Cards(self, player, enemy_card):
        x = 150
        y = 350
        if not self.player_cards[player]:  # Verifica se o jogador tem cartas
            raise ValueError(f"O jogador {player} não tem cartas para jogar.")
        for card in self.player_cards[player]:
            card_image = self.card_images[f"{card.value}_{card.suit}"]
            card_rect = card_image.get_rect()
            card_rect.topleft = (x, y)
            self.screen.blit(card_image, card_rect)
            x += 200
        # Desenha a carta do inimigo
        card_image = self.card_images[f"{enemy_card.value}_{enemy_card.suit}"]
        card_rect = card_image.get_rect()
        card_rect.topleft = (150, 50)
        self.screen.blit(card_image, card_rect)


    def check_game_winner(self, enemy_points, player_points):
        rival_points = {player: enemy_points for player in self.player_names}
        player_points = {player: player_points for player in self.player_names}
        max_points = max(player_points.values())
        for player, points in player_points.items():
            if points >= 12:
                self.winner = player
                break
        return self.winner
    
    #Verificar o vencedor da mão
    '''
        #Verifica o vencedor da mão
    def hand_winner(self, card1, card2):
        hand = Hand()
        hand.add_card(card1)
        hand.add_card(card2)
        print(f"Vencedor da rodada: {hand.winner()}")
    '''
    def hander_winner(self, player_card, enemy_card):
        hand = Hand()
        hand.add_card(player_card)
        hand.add_card(enemy_card)
        print(f"Vencedor da rodada: {hand.winner()}")


    #Verificar o vencedor da rodada
    def check_round_winner(self, player_card, enemy_card):
        winning_card = None
        round_winner = None
        # Verificação da pontuação e decisão do ganhador
        if winning_card is None or player_card.value > enemy_card.value:
            winning_card = player_card
            round_winner = self.player_names[0]
        else:
            winning_card = enemy_card
            round_winner = "PC"
        print(f"Ganhador da rodada: {round_winner}")
        return round_winner
    
    def draw(self):
        self.screen.fill(stylo.Colors.WHITE)
        self.draw_Title()
        self.draw_Text()
        self.draw_Cards(self.player_names[0], self.enemy.play())

    def run(self):
        print("Running Rodadas PC")
        self.running = True
        while self.running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_card = self.cardsnow(self.player_names[0])
                        enemy_card = self.enemy.play()
                        self.hander_winner(player_card, enemy_card)
                        self.check_round_winner(player_card, enemy_card)
                        self.running = False
            pygame.display.flip()
    


    


        
    
        



