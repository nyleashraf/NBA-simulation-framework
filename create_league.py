from nba_api.stats.static import teams
from settings import *
from team import Team
import random
from elo import Elo
import numpy as np
import pandas as pd

league = []
num_teams = season_settings['num_teams']
teams = teams.get_teams()

# create teams with NBA api module for team names
for i in range(num_teams):
    new_player_name = teams[i]['full_name']
    new_player_elo = elo_settings['init_elo']
    new_player_rting = random.gauss(season_settings['avg_rtg'], season_settings['std_dev'])
    new_player_ndg = season_settings['rtg_nudge']
    new_player = Team(new_player_name, new_player_rting, new_player_elo, new_player_ndg)
    league.append(new_player)

# create 82-game schedule for each team
# would run this function 82 times to create full league schedule
def create_matchups(league, matchups):
    # shuffle team list each iteration to create randomized schedule
    random.shuffle(league)
    # iterating through team list 15 times to create 15 matchups
    for i in range(int(len(league)//2)):
        t1 = league.pop()
        t2 = league.pop()
        pair = [t1, t2]
        matchups.append(pair)

# now running create_matchups() 82 times to create full NBA season schedule
matchups = []
for i in range(season_settings['num_games']):
    # create copy of team list each iteration so that we do not pop items from actual list
    temp_league = league.copy()
    create_matchups(temp_league, matchups)

def play_game(t1, t2):
    # calculating game score for each team with in-game variance added in
    # in-game variance allows lower-skilled teams to upset better teams on a given day
    t1_score = int(np.round(random.gauss(t1.rting, season_settings['game_var']), 0))
    t2_score = int(np.round(random.gauss(t2.rting, season_settings['game_var']), 0))

    #play game
    if t1_score > t2_score:
        t1.add_win()
        t2.add_loss()
        t1_outcome = 1

    elif t2_score > t1_score:
        t2.add_win()
        t1.add_loss()
        t1_outcome = 0

    else:
        # recursive call to play game again until winner is found
        # acts as overtime
        # is able to take regulation performance into account due to updated Elo scores (lower skilled team gets boost,
        # higher skilled team takes a hit)
        t1_outcome = play_game(t1, t2)

    # PROBLEM: t1_outcome, in certain cases, not being assigned before the following line compiles
    t2_outcome = 1 - t1_outcome


    # assigning Elo scores to new pointers -- don't think this is necessary
    t1_elo = t1.elo
    t2_elo = t2.elo

    # creating Elo class object with Elo scores, game scores, and Elo settings
    elo_obj = Elo(t1_elo, t2_elo, t1_outcome, t2_outcome, elo_settings['K'], elo_settings['beta'])

    # calculating the expected scores from team 1, team 2 given their Elo scores
    t1_elo_exp, t2_elo_exp = elo_obj.calc_expected_scores()

    # update Elo scores based on expected scores, actual scores
    t1.elo, t2.elo = elo_obj.update_elo(t1_elo_exp, t2_elo_exp)

    # calculating error in Elo predictions
    t1_elo_error = (t1_elo_exp - t1_outcome) ** 2
    t2_elo_error = (t2_elo_exp - t2_outcome) ** 2

    # updating total Elo error for each team object
    t1.elo_error += t1_elo_error
    t2.elo_error += t2_elo_error

    # utilize nudge factor to boost true rating of lower-ranked team if upset occurs
    # first scenario: t1 scores an underdog win
    if t1.rting < t2.rting and t1_score > t2_score:
        t1.nudge_rating_up()
        t2.nudge_rating_down()

    # scenario 2: t2 scores an underdog win
    elif t2.rting < t1.rting and t2_score > t1_score:
        t2.nudge_rating_up()
        t1.nudge_rating_down()

    return t1_outcome

# creating an initial dataframe with each team and their W/L record, Elo rating, true rating, Elo error
league_matrix = []
for i in range(len(league)):
    team = league[i]
    league_matrix.append(team.get_attributes())

beginning_league_df = pd.DataFrame(league_matrix, columns = ['Name', 'True Rating', 'Wins', 'Losses', 'Elo', 'Elo Error'])
beginning_league_df.sort_values(by = 'True Rating', ascending = False, inplace = True)
print(beginning_league_df)
print('Total number of games in NBA season: ', len(matchups))








