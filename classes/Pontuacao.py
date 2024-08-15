class Pontuacao:
    def __init__(self, player_names):
        self.points = {player: 0 for player in player_names}

    def adicionar_pontos(self, player, pontos):
        self.points[player] += pontos

    def get_pontos(self, player):
        return self.points.get(player, 0)