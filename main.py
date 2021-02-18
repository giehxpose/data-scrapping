import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.gosugamers.net/dota2/matches'

gosu = requests.get(url)
soup = BeautifulSoup(gosu.text, features="html.parser")
team1 = soup.find_all(attrs={'class':'team-1'})
team2 = soup.find_all(attrs={'class':'team-2'})

def match_generator(num):
    for x in num:
        yield x.get_text(strip=True)

team_list = match_generator(team1)
team_list2 = match_generator(team2)
for a,b in zip(team_list,team_list2):
    print("Upcoming Match:")
    print(f"{a} vs {b}\n")
