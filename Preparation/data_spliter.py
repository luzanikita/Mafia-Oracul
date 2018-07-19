import pandas as pd
import numpy as np
import ast

def merge_info(players, game, role):
    result = []
    
    if role == 'Citizen':
        norm_role = 1, 0
    elif role == 'Mafia':
        norm_role = 0, 0
    elif role == 'Sheriff':
        norm_role = 1, 1
    else:
        norm_role = 0, 1

    for i in ast.literal_eval(game.at[role]):
        info = players\
            .ix[players['Name'] == i[1], 1:]\
            .as_matrix()\
            .flatten()
        info = np.append(info, [i[0] / 10., *norm_role])
        result.append(info)

    return np.array(result)


def make_set(players, games):
    result = []
    roles = ['Citizen', 'Sheriff', 'Mafia', 'Don']

    for _, game in games.iterrows():
        inputs = [merge_info(players, game, role) for role in roles]
        result.append(inputs)

    return result

def main():
    players = pd.read_csv('Data/normal_stats.csv')
    games = pd.read_csv('Data/games.csv')
    players = players.iloc[:,1:]

    my_set = make_set(players, games.iloc[0:3])
    print(np.shape(my_set))

if __name__ == '__main__':
    main()