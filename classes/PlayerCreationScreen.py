import pygame
import sys
from classes.Generatorcards import ScreenCard
from stylos import stylo
from classes.Rodadas import Rodadas

class PlayerCreationScreen:
    def __init__(self, width, height):

        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.font = stylo.Fonts()
        self.input_name = ""
        self.player_names = []

        # Buttons
        self.add_button = stylo.Button(100, 450, 200, 50, stylo.Colors.RED, "Adicionar", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)
        self.remove_button = stylo.Button(400, 450, 200, 50, stylo.Colors.GREEN, "Remover", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)

        # Initialize input_boxes and box_colors
        self.input_boxes = [pygame.Rect(100, 210, 200, 50)]
        self.box_colors = [stylo.Colors.GREY]

        #Tela de criação de jogador
        self.state = "player_creation"

    def draw_background(self):
        background = pygame.image.load("data/imagem/background.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))

    def draw_textbox(self):
        textbox = stylo.TextBox(400, 50)
        textbox.draw(self.screen, (self.width // 2, self.height // 4))

    def draw_title(self):
        title = stylo.TextTitle("Jogador", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 6)
        title.draw(self.screen)

    # def draw_text(self, text, font, color, x, y):
    #     text= "Digite o nome do jogador:"
    #     text_surf = font.render(text, True, color)
    #     text_rect = text_surf.get_rect(center=(x, y))
    #     self.screen.blit(text_surf, text_rect)
    # def draw_input(self):
    #     for box, color in zip(self.input_boxes, self.box_colors):
    #         pygame.draw.rect(self.screen, color, box)
    #     font = pygame.font.Font(None, 32)
    #     text = font.render(self.input_name, True, stylo.Colors.BLACK)
    #     self.screen.blit(text, (self.input_boxes[0].x + 5, self.input_boxes[0].y + 5))
    def draw_text(self):
        font = pygame.font.Font(None, 32)
        text = font.render("Digite o nome do jogador:", True, stylo.Colors.BLACK)
        self.screen.blit(text, (100, 180))
        
    def draw_input(self):
        input_box = stylo.Input(100, 210, 200, 50, stylo.Fonts.MAIN_FONT, stylo.Colors.GREY)
        input_box.draw(self.screen)

    def draw_buttons(self):
        self.add_button.draw(self.screen)
        self.remove_button.draw(self.screen)

    def draw(self):
        self.screen.fill(stylo.Colors.WHITE)
        #self.draw_background()
        self.draw_title()
        self.draw_input()
        self.draw_buttons()
        pygame.display.flip()

    def add_player(self, player_name):
        print(f"Adicionado jogador: {player_name}")
        if player_name and player_name not in self.player_names:
            self.player_names.append(player_name)
            self.input_name = ''

    def remove_player(self):
        if self.player_names:
            self.player_names.pop()

    '''
    Main - Start the game (player_creation_screen = PlayerCreationScreen(800, 600)  
        player_creation_screen.run())
    PlayerCreationScreen - Generatorcards (player_creation_screen.players)
    Generatorcards - Rodadas (800,600,player_creation_screen.players, mao.load_card_images)
    '''

    def run(self):
        while self.state == "player_creation":
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.add_button.rect.collidepoint(event.pos):
                        self.add_player(self.input_name)
                        if len(self.player_names) >= 2:
                            #Ir para Gerador de cartas
                            self.cards = "Generator_cards"
                            self.cards = ScreenCard(self.player_names)
                            self.cards.run()
                    if self.remove_button.rect.collidepoint(event.pos):
                        self.remove_player()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.add_player(self.input_name)
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_name = self.input_name[:-1]
                    else:
                        if len(self.input_name) < 10:
                            self.input_name += event.unicode
        

