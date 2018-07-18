import pandas as pd
import numpy as np
import ast

def make_set(players, game):
    citizens = []
    mafia = []

    for i in ast.literal_eval(game.at['Citizen']):
        info = players.ix[players['Name'] == i[1], 1:].as_matrix().flatten()
        info = np.append(info, i[0] / 10.)
        citizens.append(info)

    for i in ast.literal_eval(game.at['Mafia']):
        info = players.ix[players['Name'] == i[1], 1:].as_matrix().flatten()
        info = np.append(info, i[0] / 10.)
        mafia.append(info)

    return citizens, mafia

def main():
    players = pd.read_csv('Data/normal_stats.csv')
    games = pd.read_csv('Data/games.csv')
    players = players.iloc[:,1:]

    print(make_set(players, games.iloc[0]))

if __name__ == '__main__':
    main()