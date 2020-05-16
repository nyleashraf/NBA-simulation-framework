# initialize each team in the NBA simulation as a team object to store relevant values
class Team():

    def __init__(self, name, rting, elo, ndg):
        self.name = name

        # true rating
        # using "true rating" for fake simulation to determine outcome of each game
        # in actual simulation, would use Elo ratings to determine outcome
        # because I have not yet scraped NBA Elo ratings and schedule, assigning each team an initial Elo rating
        #   of 1500, and randomly assigning "true rating" from Gaussian distribution
        self.rting = rting

        # elo score
        self.elo = elo

        # nudge factor to add variation game-over-game
        self.ndg = ndg

        self.wins = 0
        self.losses = 0

        # TODO: keep list of all Elo errors, will need to create new variable/list, plot over time
        self.elo_error = 0

        self.elo_error_list = []

    # will nudge winning team true rating if they pull off upset win
    def nudge_rating_up(self):
        self.rting += self.ndg

    # will nudge losing team true rating if they are upset by lesser team
    def nudge_rating_down(self):
        self.rting -= self.ndg

    # keeping track of win count through simulation
    def add_win(self):
        self.wins += 1

    # keeping track of loss count through simulation
    def add_loss(self):
        self.losses += 1

    def get_attributes(self):
        return [self.name, self.rting, self.wins, self.losses, self.elo, self.elo_error]