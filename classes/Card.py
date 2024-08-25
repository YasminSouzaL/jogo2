class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        self._suit = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return f'{self.value}_{self.suit}'
    
    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __repr__(self):
        return f'{self.value}_{self.suit}'