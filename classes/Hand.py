from classes.Deck import Deck
class Hand:
    def __init__(self, cards=None):
        self._cards = cards if cards else []

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value

    def add_card(self, card):
        self._cards.append(card)

    # def throw_card(self, card_position=0):
    #     if 1 <= card_position <= len(self._cards):
    #         card_position -= 1
    #         card = self._cards[card_position]
    #         self.__remove_card(card)
    #     else:
    #         if not self._cards:
    #             raise Exception("Mão vazia")
    #         else:
    #             card = self._cards[0]
    #             self.__remove_card(card)
    #     return card
    def throw_card(self, card_position=0):
        if 1 <= card_position <= len(self._cards):
            card_position -= 1
            card = self._cards[card_position]
            self.remove_card(card)
        else:
            if not self._cards:
                raise Exception("Mão vazia")
            else:
                card = self._cards[0]
                self.remove_card(card)
        return card
    
    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            print(f"Carta {card} removida com sucesso.")
        else:
            print(f"Erro: Carta {card} não encontrada na mão.")

    def __str__(self):
        return ", ".join(str(card) for card in self._cards)

    def deal_cards(self):
        deck = Deck.get_instance()
        self._cards = deck.deal(3)

    def __len__(self):
        return len(self.cards)  

    #Definir a logica do truco mineiro
    

    def winner(self):
        points = 0
        for card in self._cards:
            if card.value in ['7', 'A', '3']:
                points += 1
        return points

    def __gt__(self, other):
        return self.winner() > other.winner()

    def __lt__(self, other):
        return self.winner() < other.winner()

    def __eq__(self, other):
        return self.winner() == other.winner()