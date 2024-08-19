'''
    Criar a logica do truco

    def check_truco_winner(self, selected_cards):
        #Os dois jogadores entram em um rodada valendo 3 pontos 
        #Depois eles escolherem entre as CARTAS que ele tem na mão
        #O jogador que ganhar a rodada ganha 3 pontos
        #Cartas que o jogador tem na mão
        selected_cards = {player: None for player in self.player_names}
        for player in self.player_names:
            selected_cards[player] = self.player_cards[player][0]
        print(f"Cartas selecionadas: {selected_cards}")
        winning_card = None
        round_winner = None
        for player, card in selected_cards.items():
            if winning_card is None or card.value > winning_card.value:
                winning_card = card
                round_winner = player
        self.round_winners.append(round_winner)
        print(f"Ganhador da rodada: {round_winner}")

'''
class Truco:
    def __init__(self, player_names, selected_cards):
        self.player_names = player_names
        self.selected_cards = selected_cards
        self.round_winners = []

    def check_truco(self):
        print(f"Cartas jogadas na rodada (dentro de Truco): {self.selected_cards}")  # Verifique se isso mostra as cartas corretas
        if len(self.selected_cards) == len(self.player_names):
            winning_card = None
            round_winner = None
            for player, card in self.selected_cards.items():
                if card is not None and (winning_card is None or card.value > winning_card.value):
                    winning_card = card
                    round_winner = player
            self.round_winners.append(round_winner)
            print(f"Ganhador da rodada: {round_winner}")


