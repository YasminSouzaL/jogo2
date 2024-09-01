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
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.current_round = 0
        self.round_cards = []
        self.current_player_index = 0
        self.current_enemy_index = 0
        self.enemy_card = enemy_card
        self.pontuacao = Pontuacao(self.player_names)
        self.selected_cards = {player: None for player in self.player_names}
        self.selected_cards['PC'] = None  
        self.running = True  # Adiciona o atributo running

        print("Estou na tela RODADAPC")
        print("teste ENEMY:", self.enemy_card)
        print("Teste player:", self.player_cards)
        print("Player Names:", self.player_names)
        
    def draw_Title(self):
        title = stylo.TextTitle("Rodadas com PC", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 7)
        title.draw(self.screen)

    def draw_Text(self):
        text = stylo.Text("Vez de: " + self.player_names[self.current_player_index], stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, self.width // 2, self.height // 3)
        text.draw(self.screen)

    def draw_scoreboard(self):
        player_points = {player: self.pontuacao.get_pontos(player) for player in self.player_names}
        enemy_points = self.pontuacao.get_pontos("PC")
        
        for player, points in player_points.items():
            text = stylo.Text(f"{player}: {points} x PC: {enemy_points}", stylo.Fonts.MAIN_FONT, stylo.Colors.BLACK, self.width // 2, self.height // 5)
            text.draw(self.screen)

    def draw_Cards(self):
        x, y_player = 150, 350
        x_enemy, y_enemy = 150, 150
        self.round_cards = []
        
        # Desenha as cartas do jogador
        for card in self.player_cards[self.player_names[0]]:
            card_image = self.card_images.get(str(card))
            if card_image:
                card_rect = card_image.get_rect()
                card_rect.topleft = (x, y_player)
                self.screen.blit(card_image, card_rect)
                self.round_cards.append((card_rect, card))
                x += 200
        
        # Desenha as cartas do inimigo (viradas para baixo)
        for card in self.enemy_card['PC']:  # Corrigido aqui
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
            else:
                return 'PC'
        return None

    def enemy_turn(self):
        enemy_card = self.enemy.play()
        
        if enemy_card in self.enemy_card['PC']:
            self.enemy_card['PC'].remove(enemy_card)
            print(f"Carta {enemy_card} removida com sucesso do inimigo.")
        else:
            print(f"Erro: A carta {enemy_card} não está na lista de cartas do inimigo.")

    def draw(self):
        self.screen.fill(stylo.Colors.WHITE)
        self.draw_Title()
        self.draw_Text()
        self.draw_Cards()
        self.draw_scoreboard()
        pygame.display.flip()

    def run(self):
        print("Running RodadasPC")
        while self.running:
            self.draw()  # Atualiza a tela ao desenhar as cartas e outros elementos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for card_rect, card in self.round_cards:
                        if card_rect.collidepoint(pygame.mouse.get_pos()):
                            current_player = self.player_names[self.current_player_index]
                            print(f"Carta selecionada: {card}")

                            # Verifica se a carta está na lista do jogador antes de tentar removê-la
                            if card in self.player_cards[current_player]:
                                self.player_cards[current_player].remove(card)
                                self.selected_cards[current_player] = card
                                print(f"Carta {card} removida com sucesso.")
                                self.enemy_turn()  # Adiciona o turno do computador
                            else:
                                print(f"Erro: A carta {card} não está na lista de cartas do jogador.")

                            if all(self.selected_cards.values()):  # Verifica se ambos jogaram
                                round_winner = self.check_round_winner()
                                print(f"Vencedor da rodada: {round_winner}")
                                self.current_round += 1
                                self.selected_cards = {player: None for player in self.player_names}
                                self.selected_cards['PC'] = None

                                if all(len(cards) == 0 for cards in self.player_cards.values()):
                                    print("Acabaram as cartas")
                                    self.running = False
                                    continue
                                self.draw_scoreboard()
            pygame.time.Clock().tick(60)
        pygame.quit()
