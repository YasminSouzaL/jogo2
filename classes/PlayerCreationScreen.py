from enum import Enum, auto
import pygame
import sys
from classes.Generatorcards import ScreenCard
from stylos import stylo

class PlayerCreationState(Enum):
    PLAYER_CREATION = auto()
    GENERATOR_CARDS = auto()

class PlayerCreationScreen:
    def __init__(self, screen, width, height, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = stylo.Fonts()
        self.input_name = ""
        self.player_names = []
        self.difficulty = difficulty
        self.main_font = stylo.Fonts.get_main_font() 
        self.Title_fonte = stylo.Fonts.get_title_font()
        self.button = stylo.Fonts.get_button_font() 
        # Buttons
        self.add_button = stylo.Button(self.width/6, 450, 200, 50, stylo.Colors.RED, "Adicionar", stylo.Colors.WHITE, self.button)
        self.remove_button = stylo.Button(self.width/6 + 300, 450, 200, 50, stylo.Colors.GREEN, "Remover", stylo.Colors.WHITE, self.button)

        # Initialize input_boxes and box_colors
        self.input_boxes = [pygame.Rect(self.width/6, self.height//2.3, self.width/6 +372, 50)]
        self.box_colors = [stylo.Colors.GREY]

        #Tela de criação de jogador
        self.state = 1
        print("PlayerCreationScreen")

    def draw_background(self):
        background = pygame.image.load("data/imagem/background.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))

    def draw_title(self):
        title = stylo.TextTitle("Tela de Jogador",self.Title_fonte, stylo.Colors.RED, self.width // 2, self.height // 6)
        title.draw(self.screen)

    def draw_input(self):
        # desenha titulo e input
        title_text = stylo.Text("Digite um Jogador:", self.main_font, stylo.Colors.BLACK, self.width // 2, self.height // 3)
        title_text.draw(self.screen)

        # desenha o "box" de input
        for box, color in zip(self.input_boxes, self.box_colors):
            pygame.draw.rect(self.screen, color, box)

        font = pygame.font.Font(None, 32)
        text_surface = font.render(self.input_name, True, stylo.Colors.BLACK)
        self.screen.blit(text_surface, (self.input_boxes[0].x + 5, self.input_boxes[0].y + 5))


    def draw_buttons(self):
        self.add_button.draw(self.screen)
        self.remove_button.draw(self.screen)

    def draw(self):
        #self.screen.fill(stylo.Colors.WHITE)
        self.draw_background()
        self.draw_title()
        self.draw_input()
        self.draw_buttons()
        pygame.display.flip()

    def add_player(self, player_name):
        print(f"Adicionado jogador: {player_name}")
        # Adiciona o jogador se o nome não for vazio e não estiver na lista
        if player_name and player_name not in self.player_names:
            self.player_names.append(player_name)
            self.input_name = ''

    def remove_player(self):
        if self.player_names:
            self.player_names.pop()

    def run(self):
        while self.state == 1:
            self.draw() 
            for event in pygame.event.get():
                # saida do jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # clique
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # se clicar no botão de adicionar
                    if self.add_button.rect.collidepoint(event.pos):

                        # Adiciona o jogador
                        self.add_player(self.input_name)
                        if len(self.player_names) >= 2:
                            #Ir para Gerador de cartas
                            self.cards = ScreenCard(self.player_names, self.screen, self.state, self.difficulty)
                            self.cards.run()

                    if self.remove_button.rect.collidepoint(event.pos):
                        self.remove_player()
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.add_player(self.input_name)
                        if len(self.player_names) >= 2:
                            #Ir para Gerador de cartas
                            self.cards = ScreenCard(self.player_names, self.screen, self.state, self.difficulty)
                            self.cards.run()
                            #self.state = ""

                    elif event.key == pygame.K_BACKSPACE:
                        self.input_name = self.input_name[:-1]
                    else:
                        if len(self.input_name) < 10:
                            self.input_name += event.unicode


                            
        

