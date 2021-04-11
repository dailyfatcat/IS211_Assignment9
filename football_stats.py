#import statements
from bs4 import BeautifulSoup
import urllib3


def main():

    '''Write a script called “football_stats.py” that will load this URL,
    parse it using BeautiulSoup,
    and output the list of top 20 players, including the player’s position, team and total number of touchdowns'''

    http = urllib3.PoolManager()
    response = http.request('GET',
                            'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending')
    soup = BeautifulSoup(response.data, features='lxml')
    table = soup.find_all('tr', attrs={'class': 'TableBase-bodyTr'})

    counter = 0
    for rows in table:
        player_name = rows.find('span', attrs={'class': 'CellPlayerName--long'}).find('a').get_text()
        player_team = rows.find('span', attrs={'class': 'CellPlayerName-team'}).get_text().strip()
        player_position = rows.find('span', attrs={'class': 'CellPlayerName-position'}).get_text().strip()
        player_td = rows.find('td', attrs={'class': 'TableBase-bodyTd--number'}).get_text().strip()

        print("Name: {}".format(player_name))
        print("Team: {}".format(player_team))
        print("Positions: {}".format(player_position))
        print("Touchdowns: {}".format(player_td))
        print("\n")

        counter += 1
        if counter > 19:
            break

if __name__ == "__main__":
    main()
