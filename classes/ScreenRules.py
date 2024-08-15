import pygame
import sys
from stylos import stylo

class ScreenRules:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.button = stylo.Button(100, 400, 200, 50, stylo.Colors.RED, "Voltar", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        stylo.draw_text("Regras", self.font, stylo.Colors.BLACK, self.width / 2, 50)
        self.button.draw(screen)

    def update(self, event):
        if self.button.is_clicked(event):
            return True
        return False
