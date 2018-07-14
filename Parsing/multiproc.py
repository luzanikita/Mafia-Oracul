URL = 'https://the-mafia.net'

def get_links(link):
    return URL + link.find('a').get('href')

def get_href(a):
