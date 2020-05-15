class Team():

    def __init__(self, name, rting, elo, ndg):
        self.name = name

        # true rating
        self.rting = rting

        # elo score
        self.elo = elo

        # random nudge factor to add variation
        self.ndg = ndg

        self.wins = 0
        self.losses = 0

        self.elo_error = 0

        # used for dataframe creation
        self.list = [self.name, self.rting, self.wins, self.losses, self.elo, self.elo_error]


    def nudge_rating_up(self):
        # determines whether or not we nudge rating up or down
        # binary = random.randint(0, 1)
        # if binary == 1:
        self.rting += self.ndg

    def nudge_rating_down(self):
        self.rting -= self.ndg

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1
