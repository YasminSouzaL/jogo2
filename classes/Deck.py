from classes.Card import Card


import random


class Deck:
    CARDS_QUANTITY = 40
    _instance = None

    @staticmethod
    def get_instance():
        if Deck._instance is None:
            Deck._instance = Deck()
        return Deck._instance

    def __init__(self):
        self._cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        suits = ['Ouro', 'Copas', 'Espadas', 'Paus']
        values = ['4', '5', '6', '7', 'Q', 'J', 'K', 'As', '2', '3']
        deck = [Card(suit, value) for suit in suits for value in values]
        return deck

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, quantity):
        if len(self._cards) < quantity:
            self._cards = self.create_deck()
            self.shuffle()
        return [self._cards.pop(0) for _ in range(quantity)]

    def deal_hand(self, number_of_cards):
        if len(self._cards) < number_of_cards:
            self._cards = self.create_deck()
            self.shuffle()
        hand = self._cards[:number_of_cards]
        self._cards = self._cards[number_of_cards:]
        return hand