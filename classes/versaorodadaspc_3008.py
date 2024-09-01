import os
import pygame
from classes.Deck import Deck
from classes.Card import Card
from classes.Hand import Hand
from classes.Pontuacao import Pontuacao
from stylos import stylo

pygame.init()

class RodadasPC:
    def __init__(self, player_names, player_cards, card_images, cards_now_call_back, difficulty, width, height, enemy_card):
        self.player_names = player_names
        self.player_cards = player_cards
        self.cardsnow = cards_now_call_back
        self.difficulty = difficulty
        from classes.enemy import Enemy
        self.enemy = Enemy(self.difficulty)
        self.card_images = card_images
        self.width = width
        self.height = height
        self.player_names = list(player_cards.keys())
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.current_round = 0
        self.round_cards = []
        self.current_player_index = 0
        self.current_enemy_index = 0
        self.enemy_card = enemy_card
        self.pontuacao = None
        self.selected_card = None  # Inicializa a variável para armazenar a carta selecionada
        print("Estou na tela RODADAPC")
        print("teste ENEMY:", self.enemy_card)
        print("Teste player:", self.player_cards)

    def draw_Title(self):
        title = stylo.TextTitle("Rodadas com PC", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 7)
        title.draw(self.screen)

    def draw_Text(self):
        text = stylo.Text("Vez de: " + self.player_names[0], stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, self.width // 2, self.height // 3)
        text.draw(self.screen)

    def draw_Cards(self):
        x = 150
        y = 350 
        for player, cards in self.player_cards.items():
            for card in cards:
                if str(card) in self.card_images:
                    card_image = self.card_images[str(card)]
                    card_rect = card_image.get_rect()
                    card_rect.topleft = (x, y)
                    self.screen.blit(card_image, card_rect)
                    self.round_cards.append((card_rect, card))
                    x += 200
                else:
                    print(f"Imagem não encontrada para a carta: {str(card)}")

        x = 150
        y = 150
        for card in self.enemy_card:
            card_key = str(card)
            if card_key in self.card_images:
                card_image = self.card_images[card_key]
                card_rect = card_image.get_rect()
                card_rect.topleft = (x, y)
                self.screen.blit(card_image, card_rect)
                self.round_cards.append((card_rect, card))
                x += 200

    def hander_winner(self, player_card, enemy_card):
        hand = Hand()
        hand.add_card(player_card)
        hand.add_card(enemy_card)
        print(f"Vencedor da rodada: {hand.winner()}")

    def check_round_winner(self, player_card, enemy_card):
        winning_card = None
        round_winner = None
        if winning_card is None or player_card.value > enemy_card.value:
            winning_card = player_card
            round_winner = self.player_names[0]
        else:
            winning_card = enemy_card
            round_winner = "PC"
        print(f"Ganhador da rodada: {round_winner}")
        return round_winner

    # def handle_click(self, mouse_pos):
    #     for card_rect, card in self.round_cards:
    #         if card_rect.collidepoint(mouse_pos):
    #             self.selected_card = card
    #             print(f"Carta selecionada: {card}")
    #             break

    def handle_click(self, mouse_pos):
        for card_rect, card in self.round_cards:
            if card_rect.collidepoint(mouse_pos):
                self.selected_card = card
                print(f"Carta selecionada: {card}")
                self.remove_card_from_player(card)
                self.draw()
                break

    def remove_card_from_player(self, card):
        if card in self.player_cards[self.player_names[0]]:
            self.player_cards[self.player_names[0]].remove(card)
            print(f"Carta {card} removida do jogador {self.player_names[0]}")
        else:
            print(f"A carta {card} não foi encontrada no baralho do jogador.")


    def draw(self):
        self.screen.fill(stylo.Colors.WHITE)
        self.draw_Title()
        self.draw_Text()
        self.draw_Cards()

    def run(self):
        print("Running Rodadas PC")
        self.running = True
        while self.running:
            if len(self.player_cards[self.player_names[0]]) == 0:
                print(f"Jogador {self.player_names[0]} não tem mais cartas. Jogo encerrado.")
                self.running = False
                continue
            if len(self.enemy.hand.cards) == 0:
                print("O inimigo não tem mais cartas. Jogo encerrado.")
                self.running = False
                continue
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_card = self.cardsnow(self.player_names[0])
                        enemy_card = self.enemy.play()
                        if player_card and enemy_card:
                            self.draw_Card_Played(player_card, enemy_card)
                            round_winner = self.check_round_winner(player_card, enemy_card)
                            self.hander_winner(player_card, enemy_card)
                            self.player_cards[self.player_names[0]].remove(player_card)
                            self.enemy.hand.cards.remove(enemy_card)
                            self.draw()
                        else:
                            print("Nenhuma carta foi jogada.")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)  # Passa a posição do mouse para handle_click
            pygame.display.flip()
