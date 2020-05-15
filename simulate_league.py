from create_league import *
from settings import *
from team import *
from elo import *

import pandas as pd
import numpy as np

# iterating through entire league schedule and pulling the two team objects in each matchup pair
for i in range(len(matchups)):
    t1 = matchups[i][0]
    t2 = matchups[i][1]

    # run the play game function to determine game winner, update wins, losses, Elo
    play_game(t1, t2)

# reassigning league_matrix variable to make dataframe with final season results
league_matrix = []
for i in range(len(league)):
    team = league[i]
    league_matrix.append(team.list)

final_league_df = pd.DataFrame(league_matrix, columns = ['Name', 'True Rating', 'Wins', 'Losses', 'Elo', 'Elo Error'])
final_league_df.sort_values(by = 'True Rating', ascending = False, inplace = True)
print(final_league_df)

