import pygame
import pygame_menu
from classes.PlayerCreationScreen import PlayerCreationScreen
from classes.Player import PlayerScreen
from classes.ScreenRules import ScreenRules

#Limita a quantidade de frames por segundo
FPS = 60
#limita a qauntidade de cpu
clock = pygame.time.Clock()

class MainMenu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('JOGO DE TRUCO!!!!')
        pygame.display.set_icon(pygame.image.load("data/imagem/logo.png"))
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.difficulty = 'local'  # Define um valor padrão

    def set_difficulty(self, value, difficulty):
        # Aqui o jogador escolhe se quer jogar contra o computador ou contra outra pessoa
        self.difficulty = difficulty  
        print(f'Dificuldade definida para: {self.difficulty}')

   
    def start_the_game(self):
        if self.difficulty == 'local':
            print('Iniciar jogo contra outra pessoa')
            player_creation_screen = PlayerCreationScreen(self.surface, self.width, self.height, difficulty=0)
            player_creation_screen.run()

        elif self.difficulty == 'hard':
            print('Iniciar jogo contra o computador modo hard')
            player_screen = PlayerScreen(self.surface, self.width, self.height, difficulty=2)
            player_screen.run()

        elif self.difficulty == 'normal':
            print('Iniciar jogo contra o computador modo normal')
            player_screen = PlayerScreen(self.surface, self.width, self.height, difficulty=1)
            player_screen.run()

        else:
            print('Erro: Dificuldade não definida ou inválida.')




    def rules(self):
        screen_rules = ScreenRules(self.surface, self.width, self.height)
        screen_rules.run()

    def setup_menu(self):
        menu = pygame_menu.Menu(
            width=self.width, 
            height=self.height, 
            title='Bem vindo_Jogo de Truco', 
            theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Jogar', self.start_the_game)
        menu.add.selector('Dificuldade: ', [('Local', 'local'), ('Normal', 'normal'), ('Hard', 'hard')], onchange=self.set_difficulty)
        menu.add.button('Regras', self.rules)
        menu.add.button('Sair', pygame_menu.events.EXIT)
        menu.mainloop(self.surface)

menu = MainMenu()
menu.setup_menu()


# Adicionar getter e setters no ScreenRules.py (CORRETO)

# def set_difficulty(value, difficulty):

