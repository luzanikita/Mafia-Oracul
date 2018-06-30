import csv
import urllib.request
from bs4 import BeautifulSoup
from player import Player

def get_url(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):    
    players = {}
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", class_="tournament-table bordered")

    for row in table.find_all("tr")[1:]:
        player_info = []

        for column in row.find_all("td")[1:]:
            player_info.append(column.text.strip())

        player = Player(*player_info)
        if player.name in players.keys():
            players[player.name].merge(player)
        else:
            players[player.name] = player

    return players

def main():
    players = parse(get_url("https://new.the-mafia.net/?q=rate/sezon-2018-vtoraya-liga"))
    print(players)
    #https://new.the-mafia.net/?q=rate/sezon-2018-vtoraya-liga

if __name__ == "__main__":
    main()