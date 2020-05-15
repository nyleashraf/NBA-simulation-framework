season_settings = {
    #number of teams in league
    'num_teams': 30,
    #number of games played per season
    'num_games': 82,
    #average team rating to begin simulation
    'avg_rtg': 100,
    #standard deviation of team ratings
    'std_dev': 5,
    #game-to-game variation in rating to add randomness
    'game_var': 7.5,
    'rtg_nudge': 0.2
}

elo_settings = {
    'init_elo': 1500,
    # setting K value as 20 from 538 NBA analysis
    'K': 20,
    'beta': 400
}