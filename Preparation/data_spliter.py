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

    return np.concatenate(tuple(result))


def make_set(players, games):
    result = np.empty((0, 180), dtype=float)
    roles = ['Citizen', 'Sheriff', 'Mafia', 'Don']

    for _, game in games.iterrows():
        inputs = [merge_info(players, game, role) for role in roles]
        inputs = np.array([np.concatenate(tuple(inputs))])
        if np.shape(inputs) == (1, 180):
            result = np.append(result, inputs, axis=0)

    return np.array(result)

def main():
    players = pd.read_csv('Data/normal_stats.csv')
    games = pd.read_csv('Data/games.csv')
    players = players.iloc[:,1:]
    lenght = games.shape[0]

    test_range = list(filter(lambda x: x % 3 == 0, range(lenght)))
    training_range = list(filter(lambda x: x % 3 != 0, range(lenght)))

    testing = make_set(players, games.iloc[test_range])
    training = make_set(players, games.iloc[training_range])

    print(np.shape(testing))
    print(np.shape(training))

    np.save('Data/test', testing)
    np.save('Data/train', training)

if __name__ == '__main__':
    main()