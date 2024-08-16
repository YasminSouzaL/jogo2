import pygame
import pygame_menu
from pygame.locals import *
from classes.PlayerCreationScreen import PlayerCreationScreen
from classes.Rodadas import Rodadas
from classes.Generatorcards import ScreenCard
from classes.Winner import Winner
from classes.ScreenRules import ScreenRules

from stylos import stylo

pygame.init()
pygame.display.set_caption('JOGO DE TRUCO!!!!')
pygame.display.set_icon(pygame.image.load("data/imagem/logo.png"))

surface = pygame.display.set_mode((600, 400))

# def set_difficulty(value, difficulty):


def start_the_game():
    player_creation_screen = PlayerCreationScreen(800, 600)  
    player_creation_screen.run()

def rules():
    screen_rules = ScreenRules(800,600)
    screen_rules.run()

menu = pygame_menu.Menu(
    height=400, 
    width=600, 
    title='Bem vindo_Jogo de Truco', 
    theme=pygame_menu.themes.THEME_DARK)

menu.add.button('Jogar', start_the_game)
menu.add.button('Regras', rules)
menu.add.button('Sair', pygame_menu.events.EXIT)

menu.mainloop(surface)


