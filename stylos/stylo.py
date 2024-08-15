import pygame

# Inicialização do Pygame
pygame.init()

# Cores RGB
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (196, 213, 230)
    RED = (125, 34, 34)
    GREEN = (113, 146, 100)
    BLUE = (5, 79, 119)
    RED_CLARO = (255, 107, 102)
    VERDE_CLARO = (153, 255, 102)

# Fonte
class Fonts:
    pygame.font.init()
    MAIN_FONT = pygame.font.Font("data/font/DS-DIGIB.TTF", 32)
    CUSTOM_FONT = pygame.font.Font("data/font/stocky.ttf", 32)
    TITLE_FONT = pygame.font.Font("data/font/stocky.ttf", 36)
    BUTTON_FONT = pygame.font.Font(None, 36)

# Configurações da tela
class ScreenConfig:
    WIDTH = 750
    HEIGHT = 550
    CAPTION = 'JOGO DE TRUCO!!!!'
    ICON_PATH = "data/imagem/logo.png"

    @staticmethod
    def initialize_screen():
        screen = pygame.display.set_mode((ScreenConfig.WIDTH, ScreenConfig.HEIGHT))
        pygame.display.set_caption(ScreenConfig.CAPTION)
        logo = pygame.image.load(ScreenConfig.ICON_PATH)
        pygame.display.set_icon(logo)
        return screen
    
#Classe Textbox
class Textbox:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rect(self, center):
        return pygame.Rect(center[0] - self.width // 2, center[1] - self.height // 2, self.width, self.height)

    def draw(self, screen, center):
        rect = self.get_rect(center)
        pygame.draw.rect(screen, Colors.GREY, rect)
        return rect

# Classe Background
class Background:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.smoothscale(self.image, (ScreenConfig.WIDTH, ScreenConfig.HEIGHT))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))

# Classe Button
class Button:
    def __init__(self, x, y, width, height, color, text, text_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surf, (self.rect.x + self.rect.width / 2 - text_surf.get_width() / 2,
                                self.rect.y + self.rect.height / 2 - text_surf.get_height() / 2))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# Função para desenhar texto na tela
    def draw_text(text, rect, color, screen, font=Fonts.MAIN_FONT):
        text_surf = font.render(text, True, color)
        screen.blit(text_surf, (rect.x + rect.width / 2 - text_surf.get_width() / 2,
                                rect.y + rect.height / 2 - text_surf.get_height() / 2))
        
class TextTitle:
    def __init__(self, text, font, color, x, y):
        self.text = text
        self.font = font
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        text_surf = self.font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect(center=(self.x, self.y))
        screen.blit(text_surf, text_rect)

class TextBox:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rect(self, center):
        return pygame.Rect(center[0] - self.width // 2, center[1] - self.height // 2, self.width, self.height)

    def draw(self, screen, center):
        rect = self.get_rect(center)
        pygame.draw.rect(screen, Colors.GREY, rect)
        return rect

class Input:
    def __init__(self, x, y, width, height, font, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.color = color
        self.text = ''
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, Colors.BLACK)
        screen.blit(text_surf, (self.rect.x + 5, self.rect.y + 5))


# # Inicialização da tela
# screen = ScreenConfig.initialize_screen()
# clock = pygame.time.Clock()
#
# # Carregar imagens
# background = Background("../data/imagem/background.png")
# win_background = Background("../data/imagem/wallpaper.png")
# tela_fundo = Background("../data/imagem/tela_fundo.png")
# textbox = Background("../data/imagem/textbox.png")
#
# # Botões
# add_button = Button(100, 400, 200, 50, Colors.RED, "Adicionar", Colors.WHITE, Fonts.BUTTON_FONT)
# remove_button = Button(400, 400, 200, 50, Colors.GREEN, "Remover", Colors.WHITE, Fonts.BUTTON_FONT)
# play_button = Button(500, 200, 100, 50, Colors.BLUE, "Jogar", Colors.WHITE, Fonts.BUTTON_FONT)
#
# # Loop principal do jogo
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         if add_button.is_clicked(event):
#             print("Botão adicionar clicado!")
#         if remove_button.is_clicked(event):
#             print("Botão remover clicado!")
#         if play_button.is_clicked(event):
#             print("Botão jogar clicado!")
#
#     background.draw(screen)
#     add_button.draw(screen)
#     remove_button.draw(screen)
#     play_button.draw(screen)
#
#     pygame.display.flip()
#     clock.tick(45)
#
# pygame.quit()


def draw_text(text, rect, color, screen, font=Fonts.MAIN_FONT):
    text_surf = font.render(text, True, color)
    screen.blit(text_surf, (rect.x + rect.width / 2 - text_surf.get_width() / 2,
                            rect.y + rect.height / 2 - text_surf.get_height() / 2))