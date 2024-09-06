
import random
from classes.Deck import Deck
from classes.Hand import Hand

class Enemy:
    def __init__(self, difficulty):
        self.enemy_name = 'PC'
        self.difficulty = difficulty
        self.current_round = 0
        self.hand = Hand()
        self.initialize_hand()
        print("Estou na classe Enemy")
        print("Dificuldade na classe Enemy:", self.difficulty)

    def initialize_hand(self):
        deck = Deck()
        deck.shuffle()
        self.hand.cards = deck.deal_hand(3)  # Distribui 3 cartas para o inimigo

    def play(self, current_round):
        if not self.hand.cards:
            print("O inimigo não tem mais cartas para jogar.")
            return None

        # Seleciona a estratégia baseada na dificuldade
        if self.difficulty == 1:
            # Modo Esperto: Joga de forma estratégica
            card_to_play = self.play_smart(current_round)
        else:
            # Modo Aleatório
            card_to_play = self.play_random()

        print(f"O inimigo jogou: {card_to_play}")
        print(f"Cartas restantes do inimigo após jogada: {self.hand.cards}")
        return card_to_play

    def play_random(self):
        # Modo aleatório: Escolhe qualquer carta
        card_to_play = random.choice(self.hand.cards)
        self.hand.remove_card(card_to_play)
        return card_to_play

    def play_smart(self, current_round):
        # Ordena as cartas na mão
        sorted_cards = sorted(self.hand.cards, key=lambda card: card.value)
        
        # Se o inimigo tiver 2 ou mais cartas, joga a segunda carta
        if len(sorted_cards) > 1:
            card_to_play = sorted_cards[1]
        # Se o inimigo tiver apenas 1 carta, joga essa carta
        elif len(sorted_cards) == 1:
            card_to_play = sorted_cards[0]
        # Caso não tenha mais cartas (o que não deveria ocorrer), retorna None
        else:
            card_to_play = None
        
        return card_to_play