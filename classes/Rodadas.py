import sys
import os
from turtle import Screen 
import pygame
from classes.Winner import Winner
from classes.Hand import Hand
from classes.Pontuacao import Pontuacao
from classes.truco import Truco
from stylos import stylo
import pygame

class Rodadas:
    def __init__(self, player_names, player_cards, card_images, cards_now_call_back,difficulty, width, height):
        self.hand = Hand()
        self.running = True
        self.player_names = player_names
        self.player_cards = player_cards
        self.card_images = card_images
        self.cardsnow = cards_now_call_back
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
        
    #Trata um erro se a dificuldade se difficulty não for igual a zero
        if self.difficulty != 0:
            raise ValueError("A dificuldade deve ser 0")

    #Botões
        self.buttonTruco = stylo.ButtonTruco(self.width/6, 500, 200, 50, stylo.Colors.RED, "Truco", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)
        self.buttonAceitar = stylo.Button(self.width/6, 500, 200, 50, stylo.Colors.GREEN, "Aceitar", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)
        self.buttonCorrer = stylo.Button(self.width/6 + 300, 500, 200, 50, stylo.Colors.BLUE, "Correr", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)
    
    '''
        Comentarios para professor Alan:
            1º Professor olha que interessante se eu criar o botão Aceitar na mesma posição do botão Truco, o botão aceitar vai ser clicado quando eu clicar no botão truco
            ex: elf.buttonAceitar = stylo.Button(self.width/6, 530, 200, 50, stylo.Colors.GREEN, "Aceitar", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)
            2º Professor não posso usar o metedo check_round_winner para verificar o ganhador da rodada do truco, pois o check_round_winner só verifica o ganhador da rodada
            3º tive que criar uma classe chamada Truco para verificar o ganhador do truco
            4º Professor estou criando um sistema de pessoa contra computador
            5º temos um problema com o menu RESOVIDO
            6º Vamos fazer um teste com alguem
    
    '''

    #Desenha o título
    def draw_Title(self):
        title = stylo.TextTitle("Rodadas", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 7)
        title.draw(self.screen)
    
    #Desenha o texto
    def draw_Text(self):
        text = stylo.Text("Vez de: " + self.player_names[self.current_player_index], stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, self.width // 2, self.height // 3)
        text.draw(self.screen)
        
    def draw_background(self):
        background = pygame.image.load("data/imagem/tela_fundo.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))


    #Desenha as cartas
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

    #Desenha o placar
    def draw_scoreboard(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        text = "Placar: "
        for player, points in player_points.items():
            text += f"{player}: {points} "
        scoreboard = stylo.Text(text, stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, self.width // 2, self.height // 2)
        scoreboard.draw(self.screen)

    #Verifica o vecendor do jogo
    def check_game_winner(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        max_points = max(player_points.values())
        for player, points in player_points.items():
            if points >= 12:
                self.winner = player
                break
        return self.winner
    
    #Verifica o vencedor da mão
    def hand_winner(self, card1, card2):
        hand = Hand()
        hand.add_card(card1)
        hand.add_card(card2)
        print(f"Vencedor da rodada: {hand.winner()}")

    #Verifica o vencedor da rodada
    def check_round_winner(self):
        if len(self.selected_cards) == len(self.player_names):
            print(f"Cartas jogadas na rodada: {self.selected_cards}")
            winning_card = None
            round_winner = None

            # Verificação da pontuação e decisão do ganhador
            for player, card in self.selected_cards.items():
                if winning_card is None or card.value > winning_card.value:
                    winning_card = card
                    round_winner = player
            self.round_winners.append(round_winner)
            print(f"Ganhador da rodada: {round_winner}")

    #Lógica dos botões
    '''
        Quando o botão truco é clicado, o botão aceitar e correr aparecem
        Quando o botão aceitar é clicado, a rodada é encerrada e o jogador que aceitou ganha pontos
        Quando o botão correr é clicado, a rodada é encerrada e o jogador que correu perde pontos
        Quando o botão voltar é clicado, a rodada é encerrada e o jogador que voltou perde pontos
    
        Se o botão do truco for clicado, irá aparecer os botões de aceitar e correr para o proximo jogador
        Se o botão de aceitar for clicado, o jogador atual e o proximo jogador disparam o evento de aceitar (que é uma rodada valendo 3 pontos)
        Se o botão de correr for clicado , o jogador atual ganhar 3 pontos 
    ''' 

    # Lógica dos botões
    def button_logic(self):
        if self.truco_called:
            self.buttonAceitar.draw(self.screen)
            self.buttonCorrer.draw(self.screen)
        else:
            self.buttonTruco.draw(self.screen)

    # Lida com o truco
    def handle_truco(self):
        print("Truco foi chamado!")
        self.truco_called = True
        

    # Lida com a aceitação do truco
    def handle_aceitar(self, player_cards):
        print(f"Cartas recebidas em handle_aceitar: {player_cards}")
        Truco_screen = Truco(self.player_names, player_cards)
        Truco_screen.check_truco()


    def handle_correr(self):
        print("Jogador correu!")
        self.pontuacao.adicionar_pontos(self.player_names[self.current_player_index], 3)  # Jogador atual ganha 3 pontos
        self.end_round()


    # Finaliza a rodada
    def end_round(self):
        self.truco_called = False
        # Desenhe os botões para a próxima rodada
        self.button_logic()

    #Desenha a Tela 
    def draw(self):
        self.draw_background()
        self.draw_Title()
        self.draw_Text()
        self.draw_scoreboard()
        #Desenha as cartas de acordo com o jogador atual
        current_player = self.player_names[self.current_player_index]
        self.draw_Card(current_player)

        #Desenha os botões
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
                    # SE alguma carta for clicada
                    for card_rect, card in self.round_cards:
                        if card_rect.collidepoint(event.pos):
                            current_player = self.player_names[self.current_player_index]
                            self.selected_cards[current_player] = card  # Armazena a carta selecionada
                            self.player_cards[current_player].remove(card)
                            self.current_player_index = (self.current_player_index + 1) % len(self.player_names)

                            if all(self.selected_cards.values()):  # Verifica se todas as cartas foram selecionadas
                                self.check_round_winner()
                                round_winner = self.round_winners[-1]
                                self.pontuacao.adicionar_pontos(round_winner, 2 if self.truco_called else 1)
                                print(f"A carta vencedora foi: {self.selected_cards[round_winner]}")
                                self.current_round += 1
                                self.selected_cards = {player: None for player in self.player_names}  # Reinicializa para a próxima rodada
                                self.current_player_index = 0
                                self.truco_called = False

                                if all(len(cards) == 0 for cards in self.player_cards.values()):
                                    print("Acabaram as cartas")
                                    for player in self.player_names:
                                        pontos_faltando = 12 - self.pontuacao.get_pontos(player)
                                        print(f"Jogador {player} precisa de {pontos_faltando} pontos para ganhar")
                                    
                                    # Chamar cardsnow para gerar mais cartas
                                    self.player_cards = self.cardsnow()     
                            break

                    if self.check_game_winner():
                        self.running = False
                        # Chamar a tela winner
                        winner_screen = Winner(self.winner)
                        winner_screen.run()

                    # SE o botão de correr for clicado
                    if self.buttonCorrer.rect.collidepoint(event.pos) and self.truco_called:
                        print("Correr foi clicado")
                        self.handle_correr()

                    # SE o botão de aceitar for clicado
                    if self.buttonAceitar.rect.collidepoint(event.pos) and self.truco_called:
                        print("Aceitar foi clicado")
                        # Passar as cartas selecionadas para o método handle_aceitar
                        self.handle_aceitar(self.selected_cards)

                    # Lógica do TRUCO
                    # SE o botão de truco for clicado
                    if self.buttonTruco.rect.collidepoint(event.pos) and not self.truco_called:
                        print("ANTES DO HANDLE TRUCO")
                        self.handle_truco()

                # Fechando Jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




