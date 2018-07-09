import csv
import pandas as pd
import numpy as np

TITLES = [
    'Name',
    'Score',
    'Bonus',
    'Games',
    'Wins',
    'MVP',
    'First_blood',
    'Last_word_3',
    'Last_word_2',
    'Citizen_wins',
    'Citizen_games',
    'Mafia_wins',
    'Mafia_games',
    'Sheriff_wins',
    'Sheriff_games',
    'Don_wins',
    'Don_games'
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
    player = {
        'Name'        : name,
        'Score'       : float(score),
        'Bonus'       : float(bonus),
        'Games'       : int(games),
        'Wins'        : int(wins[:wins.index("(")]),
        'MVP'         : int(mvp),
        'First_blood' : int(first_blood),
        'Last_word_3' : int(last_word_3),
        'Last_word_2' : int(last_word_2),
    }

    player['Citizen_wins'], player['Citizen_games'] = convert_role(citizen)
    player['Mafia_wins'], player['Mafia_games'] = convert_role(mafia)
    player['Sheriff_wins'], player['Sheriff_games'] = convert_role(sheriff)
    player['Don_wins'], player['Don_games'] = convert_role(don)

    return pd.DataFrame(player, columns=TITLES, index=[0])

def convert_role(string):
        return (
            int(string[:string.index("/")]) +
            int(string[
                string.index("/") + 1:
                string.index(" ")
            ]),
            int (string[:string.index("/")])
        )

def merge_info(player1, player2):
    p1 = np.array(player1.iloc[:,1:])
    p2 = np.array(player2.iloc[:,1:])
    res = pd.DataFrame((p1 + p2), columns=TITLES[1:]) 
    res.insert(0, 'Name', player1['Name'])
    
    return res

def main():
    player1 = create_player(name="Lu")
    player2 = create_player(games=4)

    res = merge_info(player1, player2)
    res.to_csv('stat.csv')

if __name__ == "__main__":
    main()
