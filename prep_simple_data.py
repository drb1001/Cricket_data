import numpy as np, pandas as pd

data = pd.read_csv("odi_data_simple.csv", header=0)

data['team1_toss_winner'] = (data.team1 == data.toss_winner)
data['team1_winner'] = (data.team1 == data.win_team)


# check if city is home city

#
