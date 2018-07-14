import pandas as pd
import numpy as np

def make_set(players, games):
    data_set = pd.DataFrame()

players = pd.read_csv('Data/normal_stats.csv')
games = pd.read_csv('Data/games.csv')

