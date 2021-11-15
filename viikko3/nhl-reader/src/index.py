from player_reader import PlayerReader
from player_stats import PLayerStats
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PLayerStats(reader.get_players())
    nationality = "FIN"
    players = stats.top_scorers_by_nationality(nationality)
    print(f"Players from {nationality} (time: {datetime.now()}): \n")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
