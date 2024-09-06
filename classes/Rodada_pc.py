import pygame
from classes.Deck import Deck
from classes.Card import Card
from classes.Hand import Hand
from classes.Winner import Winner
from classes.enemy import Enemy
from classes.Pontuacao import Pontuacao
from stylos import stylo

class RodadasPC:
    def __init__(self, player_names, player_cards, card_images, cards_now_call_back, difficulty, width, height, enemy_card):
        self.player_names = player_names
        self.player_cards = player_cards
        self.cardsnow = cards_now_call_back
        self.difficulty = difficulty
        self.deck = Deck()
        self.enemy = Enemy(self.difficulty)
        
        self.card_images = card_images
        self.width = width
        self.height = height
        self.main_font = stylo.Fonts.get_main_font() 
        self.Title_fonte = stylo.Fonts.get_title_font() 
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.current_round = 0
        self.round_cards = []
        self.current_player_index = 0
        self.enemy_card = enemy_card
        self.pontuacao = Pontuacao(self.player_names)
        self.selected_cards = {player: None for player in self.player_names}
        self.selected_cards['PC'] = None  
        self.running = True
        self.winner = None  # Inicializar o atributo winner
        print("Estou na tela RODADAPC")

    def draw_Title(self):
        title = stylo.TextTitle("Rodadas com PC", self.Title_fonte, stylo.Colors.RED, self.width // 2, self.height // 7)
        title.draw(self.screen)

    def draw_Text(self):
        text = stylo.Text("Vez de: " + self.player_names[self.current_player_index], self.main_font, stylo.Colors.BLACK, self.width // 2, self.height // 4)
        text.draw(self.screen)

    def draw_background(self):
        background = pygame.image.load("data/imagem/tela_fundo.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))


    def draw_scoreboard(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        enemy_points = self.pontuacao.get_pontos("PC")
        
        for player, points in player_points.items():
            text = stylo.Text(f"{player}: {points} x PC: {enemy_points}", self.main_font, stylo.Colors.BLACK, self.width // 2, self.height // 5)
            text.draw(self.screen)

    def generate_new_cards(self):
        new_cards = {}
        for player in self.player_names:
            new_cards[player] = self.deck.deal_hand(3)
        return new_cards

    def draw_Cards(self):
        x, y_player = 150, 350
        x_enemy, y_enemy = 150, 170
        self.round_cards = []
        
        for card in self.player_cards[self.player_names[0]]:
            card_image = self.card_images.get(str(card))
            if card_image:
                card_rect = card_image.get_rect()
                card_rect.topleft = (x, y_player)
                self.screen.blit(card_image, card_rect)
                self.round_cards.append((card_rect, card))
                x += 200
        
        for card in self.enemy.hand.cards:
            card_image = self.card_images.get(str(card))
            if card_image:
                card_rect = card_image.get_rect()
                card_rect.topleft = (x_enemy, y_enemy)
                self.screen.blit(card_image, card_rect)
                self.round_cards.append((card_rect, card))
                x_enemy += 200

    def check_round_winner(self):
        player_card = self.selected_cards[self.player_names[0]]
        enemy_card = self.selected_cards['PC']

        if player_card and enemy_card:
            if player_card.value > enemy_card.value:
                return self.player_names[0]
            elif player_card.value < enemy_card.value:
                return 'PC'
            else:
                return 'Empate'
        return None
    
    def check_game_winner(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        player_points['PC'] = self.pontuacao.get_pontos('PC')  # Adicionar PC na verificação
        # Verificar se algum jogador ou o PC atingiu ou ultrapassou 12 pontos
        for player, points in player_points.items():
            if points >= 12:
                self.winner = player  # Armazenar o vencedor (jogador ou PC)
                return self.winner
        return None 


    def enemy_turn(self):
        if self.enemy.hand.cards:
            enemy_card = self.enemy.play(self.current_round)
            print(f"O inimigo jogou: {enemy_card}")
            if enemy_card:
                self.selected_cards['PC'] = enemy_card
            else:
                print("Erro: O inimigo não conseguiu jogar uma carta.")
        else:
            print("Erro: O inimigo não tem mais cartas para jogar.")

        print(f"Cartas restantes do inimigo: {self.enemy.hand.cards}")

    def remove_card(self, player, card):
        if card in self.player_cards[player]:
            self.player_cards[player].remove(card)
            print(f"Carta {card} removida com sucesso.")
        else:
            print(f"Erro: A carta {card} não está na lista de cartas do {player}.")
        print(f"Depois da remoção - Cartas do {player}: {self.player_cards[player]}")

    def draw(self):
        self.draw_background()
        self.draw_Title()
        self.draw_Text()
        self.draw_Cards()
        self.draw_scoreboard()
        pygame.display.flip()
    
    def run(self):
        print("Running RodadasPC")
        while self.running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    return

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for card_rect, card in self.round_cards:
                        if card_rect.collidepoint(pygame.mouse.get_pos()):
                            current_player = self.player_names[self.current_player_index]
                            print(f"Carta selecionada: {card}")
                            if card in self.player_cards[current_player]:
                                self.selected_cards[current_player] = card
                                self.remove_card(current_player, card)
                                # PC joga automaticamente após o jogador
                                self.enemy_turn()
                                if all(self.selected_cards.values()):
                                    round_winner = self.check_round_winner()
                                    print(f"Vencedor da rodada: {round_winner}")
                                    if round_winner and round_winner != 'Empate':
                                        self.pontuacao.adicionar_pontos(round_winner, 1)
                                        print(f"Pontos atualizados - {round_winner}: {self.pontuacao.get_pontos(round_winner)}")
                                    # Verificar se alguém atingiu 12 pontos e encerrar o jogo
                                    if self.check_game_winner():
                                        self.running = False
                                        winner_screen = Winner(self.winner)
                                        winner_screen.run()  # Exibir a tela de vencedor
                                        print("Fim do jogo")
                                        return  # Para garantir que o loop principal seja interrompido
                                    # Limpar as cartas selecionadas para a próxima rodada
                                    self.selected_cards = {player: None for player in self.player_names}
                                    self.selected_cards['PC'] = None
                                    # Verificar se todas as cartas foram jogadas e gerar novas cartas
                                    if all(len(cards) == 0 for cards in self.player_cards.values()):
                                        print("Acabaram as cartas")
                                        for player in self.player_names:
                                            pontos_atual = self.pontuacao.get_pontos(player)
                                            pontos_faltando = max(0, 12 - pontos_atual)
                                            print(f"Jogador {player} precisa de {pontos_faltando} pontos para ganhar")
                                        self.player_cards = self.generate_new_cards()
                                        self.enemy.hand.cards = self.deck.deal_hand(3)
                                        print(f"Novas cartas geradas para o jogador: {self.player_cards}")
                                        print(f"Novas cartas geradas para o inimigo: {self.enemy.hand.cards}")
                                break
