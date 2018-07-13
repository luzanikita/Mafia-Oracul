import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import game as G

URL = 'https://the-mafia.net'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_clubs(url):
    clubs = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    links = soup.find_all('div', class_='tournament-info-top')
    for link in links:
        clubs.append(URL + link.find('a').get('href'))

    if soup.find('li', class_='pager-next') is None:
        return clubs
    
    return clubs + get_clubs(URL +
        soup.find('li', class_='pager-next')\
            .find('a')\
            .get('href'))

def get_leagues(club_url):
    leagues = []
    html = get_html(club_url)
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('ul', class_='links-list')
        
    if links != None:
        for link in links.find_all('a'):
            leagues.append(URL + link.get('href'))

    return leagues

def get_games_url(league_url):
    html = get_html(league_url)
    soup = BeautifulSoup(html, 'lxml')
    games_url = soup.find('a', class_='btn dark-blue')
    
    if games_url != None:
        return URL + games_url.get('href')
        
def get_games(games_url):
    games = []
    html = get_html(games_url)
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', class_='games-list-wraper')   

    if div != None:
        for link in div.find_all('a'):
            games.append(URL + link.get('href'))
        
    if soup.find('li', class_='pager-next') is None:
        return games

    return games + get_games(URL +
        soup.find('li', class_='pager-next')\
            .find('a')\
            .get('href'))

def get_game_info(game_url):
    html = get_html(game_url)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_='main-game-table')
    
    if table != None:
        citizen = []
        mafia = []

        game_result = soup\
            .find('div', class_='col-right')\
            .find('dd')\
            .text\
            .strip()

        for row in table.find_all('tr', class_='col1'):
            nick = row.find('td', class_='col2').text.strip()
            role = row.find('td', class_='col5').text.strip()

            if role == "":
                citizen.append(nick)
            elif role == "М":
                mafia.append(nick)
            elif role== "Д":
                don = nick
            elif role == "Ш":
                sheriff = nick

        return G.create_game(
            game_result,
            citizen,
            mafia,
            don,
            sheriff
        )

def main():
    clubs = get_clubs(URL + '/?q=clubs_list')
    games = pd.DataFrame(columns=G.TITLES)

    for club in clubs:
        leagues = get_leagues(club)

        for league in leagues:
            try:
                games_url = get_games_url(league)

                if games_url != None:
                    games_list = get_games(games_url)

                for game in games_list:
                    
                        games = games.append(
                            get_game_info(game),
                            ignore_index=True)
            except:
                pass
        
            print(league)
    
    games.to_csv('Data/games.csv')

if __name__ == '__main__':
    main()