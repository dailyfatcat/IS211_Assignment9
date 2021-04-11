#import statements
from bs4 import BeautifulSoup
import urllib3


def main():
    '''2.	Write a script called “nfl_spreads.py” that will load this URL,
    # parse it using BeautifulSoup,
    and output the favorite, the underdog and the spread of a given game.'''

    http = urllib3.PoolManager()
    response = http.request('GET', 'http://www.footballlocks.com/nfl_point_spreads.shtml')
    soup = BeautifulSoup(response.data, features='lxml')
    table = soup.find('table', attrs={'cols': '4'})

    rows = table.find_all('tr')

    for row in rows:
        teams = row.find_all('td')
        #use a try statement in the case that the data is not well formatted
        #in this webpage the data is well formatted
        try:
            print(f'{teams[0].get_text()} |  {teams[1].get_text():20} | {teams[2].get_text():10} |  {teams[3].get_text():10}')
        except:
            print("invalid")
            continue

if __name__ == "__main__":
    main()
