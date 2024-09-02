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
        print(f"Mão inicial do inimigo: {self.hand.cards}")

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
            # Dificuldade normal: joga a carta de maior valor na primeira rodada, depois aleatório
            if current_round == 0:
                card_to_play = self.play_smart()
            else:
                card_to_play = self.play_random()
        else:
            # Outras dificuldades podem ser implementadas aqui
            card_to_play = self.play_random()

        print(f"O inimigo jogou: {card_to_play}")
        print(f"Cartas restantes do inimigo após jogada: {self.hand.cards}")
        return card_to_play

    def play_random(self):
        card_to_play = random.choice(self.hand.cards)
        self.hand.remove_card(card_to_play)
        return card_to_play

    def play_smart(self):
        # Seleciona a carta de maior valor
        card_to_play = max(self.hand.cards, key=lambda card: card.value)
        self.hand.remove_card(card_to_play)
        return card_to_play

    def get_hand(self):
        return self.hand.cards
