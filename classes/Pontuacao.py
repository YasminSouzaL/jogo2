class Pontuacao:
    def __init__(self, player_names):
        self.scores = {}
        self.points = {player: 0 for player in player_names}

    def adicionar_pontos(self, player, pontos):
        self.points[player] += pontos

    def get_pontos(self, player):
        return self.points.get(player, 0)
    
    def get_score(self, player):
        return self.scores.get(player, 0)  
