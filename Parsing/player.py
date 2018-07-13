import pandas as pd
import numpy as np

TITLES = [
    'Name',
    'Bonus',
    'Games',
    'Wins',
    'MVP',
    'First_blood',
    'Last_word_3',
    'Last_word_2',
    'Citizen_games',
    'Citizen_wins',
    'Mafia_games',
    'Mafia_wins',
    'Sheriff_games',
    'Sheriff_wins',
    'Don_games',
    'Don_wins'
]

def create_player(
    name='Гость',
    score=0.0,
    bonus=0.0,
    games=0,
    wins="0(",
    mvp=0,
    first_blood = 0,
    last_word_3=0,
    last_word_2=0,
    citizen="0/0 ",
    mafia="0/0 ",
    sheriff="0/0 ",
    don="0/0 "
):
    stats = np.array([
        bonus,
        games,
        wins[:wins.index("(")],
        mvp,
        first_blood,
        last_word_3,
        last_word_2,
        *convert_role_stats(citizen),
        *convert_role_stats(mafia),
        *convert_role_stats(sheriff),
        *convert_role_stats(don)
    ], dtype=np.float)

    return {
        'Name'  : name,
        'Stats' : stats
    }

def convert_role_stats(string):
    return (
        int(string[:string.index("/")]) +
        int(string[
            string.index("/") + 1:
            string.index(" ")
        ]),
        int (string[:string.index("/")])
    )

def merge_stats(player1, player2):
    return {
        'Name'  : player1['Name'],
        'Stats' : player1['Stats'] + player2['Stats']
    }

def split_data(player):
    return (player['Name'], *tuple(player['Stats']))

def to_df(players):
    values = list(map(split_data, players))

    return pd.DataFrame(values, columns=TITLES)