import pygame
import sys
from stylos import stylo

class ScreenRules:
    def __init__(self, screen, width, height):
        self.width = width
        self.height = height
        self.screen = screen
        self.main_font = stylo.Fonts.get_main_font() 
        self.Title_fonte = stylo.Fonts.get_title_font()
        self.button_fonte = stylo.Fonts.get_button_font() 
        self.rules_font = stylo.Fonts.get_font_rules()
        self.button = stylo.Button(100, 500, 200, 50, stylo.Colors.RED, "Voltar", stylo.Colors.WHITE,self.button_fonte )

        self.font = self.main_font
        self.__regras = [
            "Rodada: uma sequência de 4 jogadas, onde cada jogador joga uma carta;",
            "Mão: composta de duas a três rodadas, e vale inicialmente 2 pontos;",
            "Truco: proposta para subir o valor de pontos da mão para 4;",
            "Seis: proposta para subir o valor de pontos da mão para 6;",
            "Dez: proposta para subir o valor de pontos da mão para 10;",
            "Doze: proposta para subir o valor de pontos da mão para 12;",
            "Mão de 10: quando uma das duplas está com 10 pontos;",
            "Mão de ferro: quando as duas duplas estão com 10 pontos;",
            "Carta coberta: carta jogada virada , que não vale nada;",
            "Ordem das cartas (da menor para maior): 4, 5, 6, 7, Q, J, K, A, 2, 3."
        ]

    def setup_screen_color(self, screen):
        screen.fill(stylo.Colors.BLACK)


    def draw_header(self, screen):
        text = stylo.Text("Regras", self.font, stylo.Colors.GREEN, self.width / 2, 50)
        text.draw(screen)

    def draw_body(self, screen):
        text_font_to_rules = self.rules_font

        y_offset = 145
        for i, regra in enumerate(self.get_regras()):
            stylo.Text(regra, text_font_to_rules, stylo.Colors.WHITE, self.width / 2, y_offset + i * 30).draw(screen)

    def draw_footer(self, screen):
        self.button.draw(screen)

    def draw(self, screen):
        self.setup_screen_color(screen)
        self.draw_header(screen)
        self.draw_body(screen)
        self.draw_footer(screen)
        pygame.display.flip()

    def update(self, event):
        if self.button.is_clicked(event):
            return True
        return False
    
    def run(self):
        self.draw(self.screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.update(event):
                        return

    def get_regras(self):
        return self.__regras
    
    # Getters
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_screen(self):
        return self.screen

    def get_button(self):
        return self.button

    def get_font(self):
        return self.font

    def get_regras(self):
        return self.__regras

    # Setters
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_screen(self, screen):
        self.screen = screen

    def set_button(self, button):
        self.button = button

    def set_font(self, font):
        self.font = font

    def set_regras(self, regras):
        self.__regras = regras
    
