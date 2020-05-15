# creating Elo class to determine expected score given Elo ratings, update Elo score based on actual outcome
# K and beta are the arguments needed for the Elo rating calculation
# '1' and '2' refer to the two teams in a given matchup
# score1 and score2 refer to the "true rating" score with added variation to account for game randomness

class Elo():

    # need to pass in the "true rating" scores with in-game variance added (score1, score2)
    def __init__(self, elo1, elo2, score1, score2, K, beta):
        self.elo1 = elo1
        self.elo2 = elo2

        self.score1 = score1
        self.score2 = score2

        self.K = K
        self.beta = beta

    # calculate expected scores from the Elo ratings of each team
    def calc_expected_scores(self):
        exp1 = 1 / (1 + 10 ** ((self.elo2-self.elo1)/400))
        exp2 = 1 - exp1
        return exp1, exp2

    # update Elo score based on the difference between actual outcome and expected outcome
    def update_elo(self, exp1, exp2):
        updated_elo_1 = self.elo1 + self.K * (self.score1 - exp1)
        updated_elo_2 = self.elo2 + self.K * (self.score2 - exp2)
        return updated_elo_1, updated_elo_2