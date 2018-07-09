import player as pl
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Pool

URL = "https://the-mafia.net"

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_clubs(url):
    clubs = []
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    links = soup.find_all("div", class_="tournament-info-top")
    for link in links:
        clubs.append(URL + link.find("a").get("href"))

    if soup.find("li", class_="pager-next") is None:
        return clubs
    
    return clubs + get_clubs(URL +
        soup.find("li", class_="pager-next")\
            .find("a")\
            .get("href"))

def get_leagues(club_url):
    leagues = []
    html = get_html(club_url)
    soup = BeautifulSoup(html, "lxml")
    links = soup.find("ul", class_="links-list")
        
    if links != None:
        for link in links.find_all("a"):
            leagues.append(URL +
                link.get("href"))

    return leagues

def get_players_info(league_url, players=pl.create_player()):
    html = get_html(league_url)
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", class_="tournament-table bordered")
    
    if table != None:
        for row in table.find_all("tr")[1:]:
            player_info = []

            for column in row.find_all("td")[1:]:
                player_info.append(column.text.strip())

            player = pl.create_player(*player_info)
            #search_res = players['Name'].get(player.at[0, 'Name'])
            search_res = players[players['Name'] == player.at[0, 'Name']].index[0]
            if search_res != -1:
                players[player.name].merge(player)
                pl.merge_info(players.loc[players['Name'] == search_res], player)
            else:
                players = players.append(player, ignore_index=True)

    return players

def main():
    clubs = get_clubs(URL + "/?q=clubs_list")
    i = 0
    players = pl.create_player()
    for club in clubs:
        if i == 5:
            break
        leagues = get_leagues(club)
        for player in leagues:
            try:
                players = get_players_info(player, players)
            except:
                pass
        i += 1
        print(club)

    players.to_csv('maf_stat.csv')
    print(players)

if __name__ == "__main__":
    main()