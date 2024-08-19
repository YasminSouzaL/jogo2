import pygame
import pygame_menu
from pygame.locals import *
from classes.PlayerCreationScreen import PlayerCreationScreen
from classes.Player import PlayerScreen
from classes.ScreenRules import ScreenRules


'''
   Aqui na classe Main eu divido em 3 partes 
   1- Jogo de Truco uma pessoa contra outra pessoa
   2- Jogar de Truco uma pessoa contra o computador
   3 - Regras do jogo


'''

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
        self.difficulty = 'Rian'  # Define um valor padrão

    def set_difficulty(self, value, difficulty):
        # Aqui o jogador escolhe se quer jogar contra o computador ou contra outra pessoa
        self.difficulty = difficulty  
        print(f'Dificuldade definida para: {self.difficulty}')

   
    def start_the_game(self):
        
        print(self.difficulty)

        if self.difficulty == 'easy':
            print('Iniciar jogo contra outra pessoa')
            player_creation_screen = PlayerCreationScreen(self.surface, self.width, self.height)  
            player_creation_screen.run()

        if self.difficulty == 'hard':
            print('Iniciar jogo contra o computador')
            player_screen = PlayerScreen(self.surface, self.width, self.height)
            player_screen.run()
        
        else:
            print('Dificuldade não definida')
            
    def rules(self):
        screen_rules = ScreenRules(self.surface, self.width, self.height)
        screen_rules.run()

    def setup_menu(self):
        print(self.difficulty)

        menu = pygame_menu.Menu(
            width=self.width, 
            height=self.height, 
            title='Bem vindo_Jogo de Truco', 
            theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Jogar', self.start_the_game)
        menu.add.selector('Dificuldade: ', [('Easy', 'easy'),  ('Hard', 'hard')], onchange=self.set_difficulty)
        menu.add.button('Regras', self.rules)
        menu.add.button('Sair', pygame_menu.events.EXIT)

        menu.mainloop(self.surface)

menu = MainMenu()
menu.setup_menu()


# Adicionar getter e setters no ScreenRules.py

# def set_difficulty(value, difficulty):

