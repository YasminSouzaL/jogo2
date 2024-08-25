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
    def __init__(self, player_names, player_cards, card_images,cards_now_call_back,difficulty,width, height):
        self.player_names = player_names
        self.player_cards = player_cards
        self.cardsnow = cards_now_call_back
        self.difficulty = difficulty
        #Enemy é o computador ele tem suas cartas e dificuldade
        self.enemy  =  Enemy(self.difficulty)
        self.card_images = card_images
        self.width = width
        self.height = height
        self.player_names = list(player_cards.keys())
        self.screen = pygame.display.set_mode((self.width, self.height))
        print("Estou na tela RODADAPC")
        
    def draw_Title(self):
        title = stylo.TextTitle("Rodadas com PC", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 7)
        title.draw(self.screen)

    def draw_Text(self):
        text = stylo.Text("Vez de: " + self.player_names[0], stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, self.width // 2, self.height // 3)
        text.draw(self.screen)

    def draw(self):
        self.screen.fill(stylo.Colors.WHITE)
        self.draw_Title()
        self.draw_Text()
        self.draw_Cards(self.player_names[0], None)


    # player = self.player_names[0]

    #     if len(self.player_cards[player]) == 0:
    #         print(f"Jogador {player} não tem mais cartas.")
    #         return  # Saia da função `draw` se o jogador não tiver cartas.

    #     enemy_card = self.enemy.play()
    #     self.draw_Cards(player, enemy_card)

    # def draw_Cards(self, player, enemy_card):
    #     self.screen.fill(stylo.Colors.WHITE)
    #     self.draw_Text()

    #     if len(self.player_cards[player]) == 0:
    #         print(f"Jogador {player} não tem mais cartas.")
    #         return

    #     if enemy_card is None:
    #         print("O inimigo não jogou nenhuma carta.")
    #         return
        
        # player_card = self.player_cards[player].pop()
        # player_card_image = self.card_images[player_card.__str__()]
        # enemy_card_image = self.card_images[enemy_card.__str__()]
        # self.screen.blit(player_card_image, (self.width // 4, self.height // 2))
        # self.screen.blit(enemy_card_image, (self.width // 2, self.height // 2))

    def draw_Cards(self, player, enemy_card):
        self.screen.fill(stylo.Colors.WHITE)
        self.draw_Text()

        if len(self.player_cards[player]) == 0:
            print(f"Jogador {player} não tem mais cartas.")
            return

        if enemy_card is None:
            print("O inimigo não jogou nenhuma carta.")
            return

        player_card = self.player_cards[player].pop()
        print(f"Jogador {player} jogou: {player_card}")
        player_card_image = self.card_images[player_card.__str__()]
        enemy_card_image = self.card_images[enemy_card.__str__()]
        self.screen.blit(player_card_image, (self.width // 4, self.height // 2))
        self.screen.blit(enemy_card_image, (self.width // 2, self.height // 2))


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
    
    def run(self):
        print("Running Rodadas PC")
        self.running = True
        while self.running:
            if len(self.player_cards[self.player_names[0]]) == 0:
                print(f"Jogador {self.player_names[0]} não tem mais cartas. Jogo encerrado.")
                self.running = False
                continue # Pule o restante do loop e vá para a próxima iteração.
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
            pygame.display.flip()


    # def run(self):
    #     print("Running Rodadas PC")
    #     self.running = True
    #     while self.running:
    #         self.draw()
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 self.running = False
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     player_card = self.cardsnow(self.player_names[0])
    #                     enemy_card = self.enemy.play()
    #                     self.hander_winner(player_card, enemy_card)
    #                     self.check_round_winner(player_card, enemy_card)
    #                     self.running = False
    #         pygame.display.flip()