import sys

import pygame
from classes.Hand import Hand
from classes.Pontuacao import Pontuacao
from stylos import stylo
#Recebe os nomes de PlayerCreationScreen e as cartas de ScreenCard
class Rodadas:
    def __init__(self,player_names, player_cards, card_images, cardsnow):
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
    
    def draw_textbox(self, screen, width, height):
        textbox = stylo.TextBox(400, 50)
        textbox.draw(screen, (width // 2, height // 4))
        return textbox

    def draw_title(self):
        title = stylo.TextTitle("Rodadas", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 6)
        title.draw(self.screen)
    
    def draw_text(self, screen, text, font, color, x, y):
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=(x, y))
        screen.blit(text_surf, text_rect)

    def square_pontos(self, screen, x, y, width, height, color):
        pygame.draw.rect(screen, color, (x - width // 3, y - height // 2, width, height))

    def draw_players(self, screen, main_font):
        y = 350
        for player in self.player_names:
            self.square_pontos(screen, 150, y, 250, 60, stylo.Colors.VERDE_CLARO)
            points = self.pontuacao.get_pontos(player)
            self.draw_text(screen, f"{player} - {points} pontos", main_font, stylo.Colors.BLACK, 180, y)
            y += 60

    def draw_truco_button(self, screen):
        truco_button = pygame.Rect(550, 400, 150, 50)
        pygame.draw.rect(screen, stylo.Colors.RED, truco_button)
        self.draw_text(screen, 'TRUCO', stylo.Fonts.BUTTON_FONT, stylo.Colors.WHITE, truco_button.centerx, truco_button.centery)
        return truco_button

    def draw_cards(self, screen, player):
        x = 100
        y = 140
        for card in self.player_cards[player]:
            card_image = self.card_images[str(card)]
            card_rect = card_image.get_rect(topleft=(x, y))
            screen.blit(card_image, card_rect)
            self.round_cards.append((card_rect, card))
            x += self.card_width

    def draw(self, screen, tela_fundo):
        screen.blit(tela_fundo, (0, 0))
        self.draw_title(screen, stylo.textbox, stylo.Fonts.MAIN_FONT, stylo.ScreenConfig.WIDTH, stylo.ScreenConfig.HEIGHT)
        current_player = self.player_names[self.current_player_index]
        self.draw_text(screen, f"Vez de {current_player}", stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, 330, 120)
        self.draw_cards(screen, current_player)
        self.draw_players(screen, stylo.Fonts.MAIN_FONT)
        truco_button = self.draw_truco_button(screen)
        pygame.display.flip()
        return truco_button

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

    def check_game_winner(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        max_points = max(player_points.values())
        for player, points in player_points.items():
            if points >= 12:
                self.winner = player
                break
        return self.winner

    def handle_truco(self):
        self.truco_called = True
        print("Truco foi chamado!")
        if self.truco_called:
            self.pontuacao.adicionar_pontos(self.player_names[self.current_player_index], 3)
            self.current_player_index = (self.current_player_index + 1) % len(self.player_names)
            self.selected_cards = {player: [] for player in self.player_names}
            self.truco_called = False

    def run(self):
        self.running = True
        self.selected_cards = {player: [] for player in self.player_names}
        self.pontuacao = Pontuacao(self.player_names)
        screen = stylo.ScreenConfig.initialize_screen()
        clock = pygame.time.Clock()
        tela_fundo = pygame.image.load("data/imagem/tela_fundo.png")
        tela_fundo = pygame.transform.scale(tela_fundo, (stylo.ScreenConfig.WIDTH, stylo.ScreenConfig.HEIGHT))

        while self.running:
            self.round_cards = []
            truco_button = self.draw(screen, tela_fundo)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if truco_button.collidepoint(event.pos):
                        self.handle_truco()
                    else:
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
                                    self.selected_cards = {player: [] for player in self.player_names}
                                    self.current_player_index = 0
                                    self.truco_called = False
                                    if all(len(cards) == 0 for cards in self.player_cards.values()):
                                        print("Acabaram as cartas")
                                        for player in self.player_names:
                                            pontos_faltando = 12 - self.pontuacao.get_pontos(player)
                                            print(f"Jogador {player} precisa de {pontos_faltando} pontos para ganhar")
                                            #Chamar o cardsnow para gerar novas cartas
                                            self.cardsnow(player)
                                        self.running = False

                                            

                                break
                    if self.check_game_winner():
                        self.running = False

    def start_game(self, player_names):
        self.player_names = player_names
        self.run()


