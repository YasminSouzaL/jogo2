import sys
import os
from turtle import Screen 
import pygame
from classes.Winner import Winner
from classes.Hand import Hand
from classes.Deck import Deck
from classes.Pontuacao import Pontuacao
from classes.truco import Truco
from stylos import stylo
import pygame
pygame.mixer.init() 


class Rodadas:
    def __init__(self, player_names, player_cards, card_images, cards_now_call_back, difficulty, width, height):
        self.hand = Hand()
        self.deck = Deck()
        self.running = True
        self.player_names = player_names
        self.player_cards = player_cards
        self.card_images = card_images
        self.cards_now_call_back = cards_now_call_back 
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
        self.difficulty = difficulty
        self.main_font = stylo.Fonts.get_main_font() 
        self.Title_fonte = stylo.Fonts.get_title_font()
        self.button = stylo.Fonts.get_button_font() 
        
        self.truco_sound = pygame.mixer.Sound("data/music/truco.mp3")
        self.aceitar_sound = pygame.mixer.Sound("data/music/aceita.mp3")
        self.correr_sound = pygame.mixer.Sound("data/music/correu.mp3")
        
        if self.difficulty != 0:
            raise ValueError("A dificuldade deve ser 0")

        self.buttonTruco = stylo.ButtonTruco(self.width/6, 500, 200, 50, stylo.Colors.RED, "Truco", stylo.Colors.WHITE, self.button)
        self.buttonAceitar = stylo.Button(self.width/6, 500, 200, 50, stylo.Colors.GREEN, "Aceitar", stylo.Colors.WHITE, self.button)
        self.buttonCorrer = stylo.Button(self.width/6 + 300, 500, 200, 50, stylo.Colors.BLUE, "Correr", stylo.Colors.WHITE, self.button)

    def generate_new_cards(self):
        new_cards = {}
        for player in self.player_names:
            new_cards[player] = self.deck.deal_hand(3)
        return new_cards

    def draw_Title(self):
        title = stylo.TextTitle("Rodadas", self.Title_fonte, stylo.Colors.RED, self.width // 2, self.height // 7)
        title.draw(self.screen)

    def draw_Text(self):
        text = stylo.Text("Vez de: " + self.player_names[self.current_player_index], self.main_font, stylo.Colors.BLACK, self.width // 2, self.height // 4)
        text.draw(self.screen)

    def draw_background(self):
        background = pygame.image.load("data/imagem/tela_fundo.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))

    # def draw_Card(self, player):
    #     x = 150
    #     y = 350
    #     for card in self.player_cards[player]:
    #         card_image = self.card_images[f"{card.value}_{card.suit}"]
    #         card_rect = card_image.get_rect()
    #         card_rect.topleft = (x, y)
    #         self.screen.blit(card_image, card_rect)
    #         self.round_cards.append((card_rect, card))
    #         x += 200

    def draw_Card(self, player):
        x = 150
        y = 350
        for card in self.player_cards[player]:
            card_image = self.card_images[f"{card.value}_{card.suit}"]
            
            # Criação de um objeto da classe Cards para desenhar a carta
            card_obj = stylo.Cards(self.screen, x, y, card_image.get_width(), card_image.get_height(), card_image)
            
            # Atualiza a lista de cartas da rodada (round_cards)
            self.round_cards.append((card_obj.card_rect, card))
            
            x += 220  # Incrementa a posição horizontal para a próxima cart

    def draw_scoreboard(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        text = "Placar: "
        for player, points in player_points.items():
            text += f"{player}: {points} "
        scoreboard = stylo.Text(text, self.main_font, stylo.Colors.BLACK, self.width // 2, self.height // 3)
        scoreboard.draw(self.screen)

    def check_game_winner(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        max_points = max(player_points.values())
        for player, points in player_points.items():
            if points >= 12:
                self.winner = player
                break
        return self.winner

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

    def button_logic(self):
        if self.truco_called:
            self.buttonAceitar.draw(self.screen)
            self.buttonCorrer.draw(self.screen)
        else:
            self.buttonTruco.draw(self.screen)

    def handle_truco(self):
        print("Truco foi chamado!")
        self.truco_called = True

    def handle_aceitar(self, player_cards):
        print(f"Cartas recebidas em handle_aceitar: {player_cards}")
        Truco_screen = Truco(self.player_names, player_cards)
        Truco_screen.check_truco()

    def handle_correr(self):
        print("Jogador correu!")
        self.pontuacao.adicionar_pontos(self.player_names[self.current_player_index], 3)
        self.end_round()

    def end_round(self):
        self.truco_called = False
        self.button_logic()

    def draw(self):
        self.draw_background()
        self.draw_Title()
        self.draw_Text()
        self.draw_scoreboard()
        current_player = self.player_names[self.current_player_index]
        self.draw_Card(current_player)
        self.button_logic()
        pygame.display.flip()

    def run(self):
        print("Running Rodadas")
        self.pontuacao = Pontuacao(self.player_names)
        self.selected_cards = {player: None for player in self.player_names}
        while self.running:
            self.round_cards = []
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for card_rect, card in self.round_cards:
                        if card_rect.collidepoint(event.pos):
                            current_player = self.player_names[self.current_player_index]
                            self.selected_cards[current_player] = card
                            self.player_cards[current_player].remove(card)
                            self.current_player_index = (self.current_player_index + 1) % len(self.player_names)

                            if all(self.selected_cards.values()):
                                self.check_round_winner()
                                round_winner = self.round_winners[-1]
                                self.pontuacao.adicionar_pontos(round_winner, 2 if self.truco_called else 1)
                                print(f"A carta vencedora foi: {self.selected_cards[round_winner]}")
                                self.current_round += 1
                                self.selected_cards = {player: None for player in self.player_names}
                                self.current_player_index = 0
                                self.truco_called = False

                                if all(len(cards) == 0 for cards in self.player_cards.values()):
                                    print("Acabaram as cartas")
                                    for player in self.player_names:
                                        pontos_faltando = 12 - self.pontuacao.get_pontos(player)
                                        print(f"Jogador {player} precisa de {pontos_faltando} pontos para ganhar")

                                    self.player_cards = self.generate_new_cards()
                            break

                    if self.check_game_winner():
                        self.running = False
                        winner_screen = Winner(self.winner)
                        winner_screen.run()

                    if self.buttonCorrer.rect.collidepoint(event.pos) and self.truco_called:
                        print("Correr foi clicado")
                        self.correr_sound.play()
                        self.handle_correr()
                    

                    if self.buttonAceitar.rect.collidepoint(event.pos) and self.truco_called:
                        print("Aceitar foi clicado")
                        self.aceitar_sound.play()
                        self.handle_aceitar(self.selected_cards)

                    if self.buttonTruco.rect.collidepoint(event.pos) and not self.truco_called:
                        #Toca o audio 
                        self.truco_sound.play()
                        self.handle_truco()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




