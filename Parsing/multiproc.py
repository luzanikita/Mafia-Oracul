import games_parser as gp
import pandas as pd
from multiprocessing import Pool

URL = 'https://the-mafia.net'

def get_links(link):
    return URL + link.find('a').get('href')

def map_games(game):
    return gp.get_game_info(game)

def map_leagues(league):
    try:
        games_url = gp.get_games_url(league)
        
        if games_url != None:
            return gp.get_games(games_url)
        else:
            return []
    
    except:
        return []

def map_clubs(club):
    return gp.get_leagues(club)