import pygame
from stylos import stylo

class Winner:
    def __init__(self, winner):
        self.winner = winner
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.Main_fonte = stylo.Fonts.get_main_font()
        self.title_fonte = stylo.Fonts.get_title_font()
        self.button = stylo.Button(100, 400, 200, 50, stylo.Colors.RED, "Menu", stylo.Colors.WHITE, self.Main_fonte)

    def backgound(self):
        background = pygame.image.load("data/imagem/wallpaper.png")
        background = pygame.transform.smoothscale(background, (self.width, self.height))
        self.screen.blit(background, (0, 0))

    #Voltar para a Main.py
    def button_menu(self):
        return self.button.is_over(pygame.mouse.get_pos())

    
    def draw(self, screen):
        self.backgound()
        stylo.TextTitle("Vencedor", self.title_fonte, stylo.Colors.RED, self.width // 2, self.height // 6).draw(screen)
        stylo.Text(f"O vencedor é: {self.winner}", self.title_fonte, stylo.Colors.BLACK, self.width // 2, self.height // 3).draw(screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_menu():
                        running = False
            self.draw(self.screen)
            self.button.draw(self.screen)
            pygame.display.flip()

        pygame.quit()