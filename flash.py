import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match-schedules')
def match():
    url = 'https://www.gosugamers.net/dota2/matches'
    gosu = requests.get(url)
    soup = BeautifulSoup(gosu.text, features="html.parser")
    team1 = soup.find_all(attrs={'class': 'team-1'})
    team2 = soup.find_all(attrs={'class': 'team-2'})

    def match_generator(num):
        for x in num:
            yield x #.get_text(strip=True)

    team_list = match_generator(team1)
    team_list2 = match_generator(team2)
    x = zip(team_list,team_list2)
    return render_template('data_scrap.html', team_list=team_list, team_list2=team_list2, x=x)

@app.route('/idr-rates')
def rates():
    rates = requests.get('http://www.floatrates.com/daily/idr.json')
    data = rates.json()
    return render_template('rates.html', data=data.values())


if __name__ == '__main__':
    app.run(debug=True)