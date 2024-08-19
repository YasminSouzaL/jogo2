import pygame
from stylos import stylo

class Winner:
    def __init__(self, winner):
        self.winner = winner
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 55)
        self.button = stylo.Button(100, 400, 200, 50, stylo.Colors.RED, "Voltar", stylo.Colors.WHITE, stylo.Fonts.BUTTON_FONT)

    def backgound(self):
        background = pygame.image.load("data/imagem/wallpaper.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))

    def draw(self, screen):
        self.backgound()
        stylo.TextTitle("Vencedor", stylo.Fonts.TITLE_FONT, stylo.Colors.RED, self.width // 2, self.height // 6).draw(screen)
        stylo.Text(f"O vencedor é: {self.winner}", self.font, stylo.Colors.BLACK, self.width // 2, self.height // 3).draw(screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        return
            self.draw(self.screen)
            self.button.draw(self.screen)
            pygame.display.flip()