class Elo():

    # need to pass in the in-game scores with variance added
    def __init__(self, elo1, elo2, score1, score2, K, beta):
        self.elo1 = elo1
        self.elo2 = elo2

        self.score1 = score1
        self.score2 = score2

        self.K = K
        self.beta = beta

    def calc_expected_scores(self):
        exp1 = 1 / (1 + 10 ** ((self.elo2-self.elo1)/400))
        exp2 = 1 - exp1
        return exp1, exp2

    def update_elo(self, exp1, exp2):
        updated_elo_1 = self.elo1 + self.K * (self.score1 - exp1)
        updated_elo_2 = self.elo2 + self.K * (self.score2 - exp2)
        return updated_elo_1, updated_elo_2