import sys
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
        text = stylo.TextTitle("Vez de ...", stylo.Fonts.BUTTON_FONT, stylo.Colors.BLACK, 380, 130)
        text.draw(self.screen)

    def draw_background(self):
        background = pygame.image.load("data/imagem/background.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))

    def draw_players(self):
        y = 350
        for player in self.player_names:
            square = stylo.SquarePonts(150,300,stylo.Colors.VERDE_CLARO)

    def draw_cards(self):
        #Desenhar as cartas dos jogadores 
        x = 100
        y = 200
        for player, cards in self.player_cards.items():
            for card in cards:
                card_image = self.card_images[f"{card.value}_{card.suit}"]
                card_image_rect = card_image.get_rect(center=(x, y))
                self.screen.blit(card_image, card_image_rect)
                self.round_cards.append((card_image_rect, card))
                x += 200
            x = 100
            y += 200


    def draw_handleTruco(self):
        truco_button = stylo.TextBox(100, 50)
        truco_button_rect = truco_button.draw(self.screen, (330, 500))
        truco_text = stylo.Text("Truco", stylo.Fonts.BUTTON_FONT, stylo.Colors.BLACK, 330, 500)
        truco_text.draw(self.screen)
        return truco_button_rect
    

    def draw(self):
        self.screen.fill(stylo.Colors.WHITE)
        self.draw_Title()
        self.draw_text()
        self.draw_cards()

        pygame.display.flip()

    def run(self):
        self.running = True
        self.draw()
        print("Estou na tela de rodadas")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


    # def draw_players(self, screen, main_font):
    #     y = 350
    #     for player in self.player_names:
    #         self.square_pontos(screen, 150, y, 250, 60, stylo.Colors.VERDE_CLARO)
    #         points = self.pontuacao.get_pontos(player)
    #         self.draw_text(screen, f"{player} - {points} pontos", main_font, stylo.Colors.BLACK, 180, y)
    #         y += 60

    # def square_pontos(self, screen, x, y, width, height, color):
    #     pygame.draw.rect(screen, color, (x - width // 3, y - height // 2, width, height))
    # def draw_truco_button(self):
    #     truco_button = stylo.TextBox(100, 50)
    #     truco_button_rect = truco_button.draw(self.screen, (330, 500))
    #     truco_text = stylo.Text("Truco", stylo.Fonts.BUTTON_FONT, stylo.Colors.BLACK, 330, 500)
    #     truco_text.draw(self.screen)
    #     return truco_button_rect

    # def draw_text(self):
    #     text = stylo.TextTitle("Vez de", stylo.Fonts.BUTTON_FONT, stylo.Colors.BLACK, 330, 120)
    #     text.draw(self.screen)

    # def draw(self, screen, tela_fundo):
    #     screen.blit(tela_fundo, (0, 0))
    #     self.draw_Title()
    #     current_player = self.player_names[self.current_player_index]
    #     self.draw_text()
    #     self.draw_cards(screen, current_player)
    #     self.draw_players(screen, stylo.Fonts.MAIN_FONT)
    #     truco_button = self.draw_truco_button(screen)
    #     pygame.display.flip()
    #     return truco_button
    
    # def hand_winner(self, card1, card2):
    #     hand = Hand()  
    #     hand.add_card(card1)
    #     hand.add_card(card2)
    #     print(f"Vencedor da rodada: {hand.winner()}")

    # def check_round_winner(self):
    #     if len(self.selected_cards) == len(self.player_names):
    #         print(f"Cartas jogadas na rodada: {self.selected_cards}")
    #         winning_card = None
    #         round_winner = None
    #         for player, card in self.selected_cards.items():
    #             if winning_card is None or card.value > winning_card.value:
    #                 winning_card = card
    #                 round_winner = player
    #         self.round_winners.append(round_winner)
    #         print(f"Ganhador da rodada: {round_winner}")

    # def check_game_winner(self):
    #     player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
    #     max_points = max(player_points.values())
    #     for player, points in player_points.items():
    #         if points >= 12:
    #             self.winner = player
    #             break
    #     return self.winner

    # def handle_truco(self):
    #     self.truco_called = True
    #     print("Truco foi chamado!")
    #     if self.truco_called:
    #         self.pontuacao.adicionar_pontos(self.player_names[self.current_player_index], 3)
    #         self.current_player_index = (self.current_player_index + 1) % len(self.player_names)
    #         self.selected_cards = {player: [] for player in self.player_names}
    #         self.truco_called = False

    # def run(self):
    #     self.running = True
    #     self.selected_cards = {player: [] for player in self.player_names}
    #     self.pontuacao = Pontuacao(self.player_names)
    #     screen = stylo.ScreenConfig.initialize_screen()
    #     clock = pygame.time.Clock()
    #     tela_fundo = pygame.image.load("data/imagem/tela_fundo.png")
    #     tela_fundo = pygame.transform.scale(tela_fundo, (stylo.ScreenConfig.WIDTH, stylo.ScreenConfig.HEIGHT))

    #     while self.running:
    #         self.round_cards = []
    #         truco_button = self.draw(screen, tela_fundo)
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if truco_button.collidepoint(event.pos):
    #                     self.handle_truco()
    #                 else:
    #                     for card_rect, card in self.round_cards:
    #                         if card_rect.collidepoint(event.pos):
    #                             current_player = self.player_names[self.current_player_index]
    #                             self.selected_cards[current_player] = card
    #                             self.player_cards[current_player].remove(card)
    #                             self.current_player_index = (self.current_player_index + 1) % len(self.player_names)
    #                             if all(self.selected_cards.values()):
    #                                 self.check_round_winner()
    #                                 round_winner = self.round_winners[-1]
    #                                 self.pontuacao.adicionar_pontos(round_winner, 2 if self.truco_called else 1)
    #                                 print(f"A carta vencedora foi: {self.selected_cards[round_winner]}")
    #                                 self.current_round += 1
    #                                 self.selected_cards = {player: [] for player in self.player_names}
    #                                 self.current_player_index = 0
    #                                 self.truco_called = False
    #                                 if all(len(cards) == 0 for cards in self.player_cards.values()):
    #                                     print("Acabaram as cartas")
    #                                     for player in self.player_names:
    #                                         pontos_faltando = 12 - self.pontuacao.get_pontos(player)
    #                                         print(f"Jogador {player} precisa de {pontos_faltando} pontos para ganhar")
    #                                         #Chamar o cardsnow para gerar novas cartas
    #                                         self.cardsnow(player)
    #                                     self.running = False

                                            

    #                             break
    #                 if self.check_game_winner():
    #                     self.running = False

    # def start_game(self, player_names):
    #     self.player_names = player_names
    #     self.run()


