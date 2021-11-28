class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def _get_score_names(self, score_number):
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_names[score_number]

    def won_point(self, player_name):
        if self.player1_name == player_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1
    
    def _create_answer(self, situation):
        if situation == 0:
            if self.m_score1 < 4:
                score_name = self._get_score_names(self.m_score1)
                return f"{score_name}-All"
            else:
                return "Deuce"
        
        elif situation < 0:
            if self.m_score2 < 4:
                player1_score_name = self._get_score_names(self.m_score1)
                player2_score_name = self._get_score_names(self.m_score2)
                return f"{player1_score_name}-{player2_score_name}"
            elif situation == -1:
                return f"Advantage {self.player2_name}"
            else:
                return f"Win for {self.player2_name}"
        
        else:
            if self.m_score1 < 4:
                player1_score_name = self._get_score_names(self.m_score1)
                player2_score_name = self._get_score_names(self.m_score2)
                return f"{player1_score_name}-{player2_score_name}"
            elif situation == 1:
                return f"Advantage {self.player1_name}"
            else:
                return f"Win for {self.player1_name}"            

    def get_score(self):
        situation = self.m_score1 - self.m_score2
        return self._create_answer(situation)
