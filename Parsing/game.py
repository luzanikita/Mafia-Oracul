import pandas as pd
import numpy as np

TITLES = [
    'Game_result',
    'Citizen',
    'Mafia',
    'Don',
    'Sheriff'
]

def create_game(
    game_result='город',
    citizen=['Гость' for i in range(6)],
    mafia=['Гость' for i in range(2)],
    don='Гость',
    sheriff='Гость'
):
    return pd.DataFrame(
        [(game_result, citizen, mafia, don, sheriff)],
        columns=TITLES)

def main():
    games = pd.DataFrame(columns=TITLES)

    for i in range(10):
        games = games.append(create_game(), ignore_index=True)

    games.to_csv('games.csv')

if __name__ == '__main__':
    main()