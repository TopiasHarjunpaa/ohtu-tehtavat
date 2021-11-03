import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReaderStub()
        self.players = self.reader.get_players()
        self.statistics = Statistics(self.reader)
    
    def test_search_player_by_name(self):
        player1 = self.statistics.search("Semenko")
        player2 = self.statistics.search("Koivu")
        self.assertEqual(self.players[0].name,player1.name)
        self.assertIsNone(player2)
    
    def test_search_by_team_name(self):
        players_of_team1 = self.statistics.team("EDM")
        players_of_team2 = self.statistics.team("AAA")
        players_of_team3 = self.statistics.team("PIT")
        self.assertEqual(len(players_of_team1), 3)
        self.assertEqual(len(players_of_team2), 0)
        self.assertEqual(len(players_of_team3), 1)
        self.assertEqual(players_of_team3[0].name, "Lemieux")

    def test_top_scorers(self):
        sorted_players1 = self.statistics.top_scorers(5)
        sorted_players2 = self.statistics.top_scorers(1)
        sorted_players3 = self.statistics.top_scorers(0)
        sorted_players4 = self.statistics.top_scorers(100)
        self.assertEqual(len(sorted_players1), 5)
        self.assertEqual(len(sorted_players2), 1)
        self.assertEqual(len(sorted_players3), 0)
        self.assertEqual(len(sorted_players4), 5)
        self.assertEqual(sorted_players1[0].points, 124)
        self.assertEqual(sorted_players1[4].points, 16)
