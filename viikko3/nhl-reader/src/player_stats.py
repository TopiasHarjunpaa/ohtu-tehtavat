
class PLayerStats:
    def __init__(self, players):
        self.players = players
    
    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda p: p.nationality == nationality, self.players)

        return sorted(filtered_players, reverse=True ,key=sort_by_points)

def sort_by_points(player):
    return player.points