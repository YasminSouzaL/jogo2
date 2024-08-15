import pygame
from abc import ABC, abstractmethod
from stylos.stylo import *

pygame.init()
        
class GameContract(ABC):
    '''
        Classe abstrata que define os métodos que
        devem ser implementados pelas classes que a herdam.
    '''
    @property
    @abstractmethod
    def draw_title(self):
        pass

    @abstractmethod
    def draw_input(self):
        pass

    @abstractmethod
    def draw_buttons(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def switch_screen(self):
        pass
