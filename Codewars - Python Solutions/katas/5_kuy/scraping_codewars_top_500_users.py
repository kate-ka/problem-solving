"""
You should get and parse the html of the https://www.codewars.com/users/leaderboard.
Return a 'Leaderboard' object with a position property.
Leaderboard#position should contain 500 'User' objects.
Leaderboard#position[i] should return the ith ranked User(1 based index).
Each User should have the following properties:

User#name    # => the user's username, not their real name
User#clan    # => the user's clan, empty string if empty clan field
User#honor   # => the user's honor points as an integer
Ex:

  an_alien = leaderboard.position[3]   # => #<User:0x3124da0 @name="myjinxin2015", @clan="China Changyuan", @honor=21446>
  an_alien.name                        # => "myjinxin2015"
  an_alien.clan                        # => "China Changyuan"
  an_alien.honor                       # => 21446

"""

from bs4 import BeautifulSoup
import requests

Url = 'https://www.codewars.com/users/leaderboard'

class Leaderboard:
    def __init__(self, position):
        self.position = position


class User:
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = clan
        self.honor = honor


def solution():

    html_doc = requests.get(Url).text
    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.find("table")
    positions = {}
    i = 1
    for row in table.find_all("tr")[1:]:
        clan, honor = row.find_all("td")[-2:]
        name = row.attrs['data-username']

        positions[i] = User(name, clan.text, int(honor.text))
        i += 1
    return Leaderboard(positions)