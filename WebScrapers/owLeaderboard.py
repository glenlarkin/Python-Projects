import requests
from bs4 import BeautifulSoup

# get the data for Overwatch leaderboards
data = requests.get('https://overwatch.op.gg/leaderboards?platform=pc')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('table', { 'class': 'LeaderBoardsTable' })
tbody = leaderboard.find('tbody')

filename = "OverwatchLeaders.csv"           # creates .csv file named products
f = open(filename, "w")             # opens file for input

headers = "Postion, Skill Rating, Game Level, K:D Ratio, Win Percentage, Time Played \n"             # table Head dividers
percent = '%'
f.write(headers)

for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    username = tr.find_all('td')[2].find('b').text.strip()
    skillRating = tr.find_all('td')[3].text.strip()
    gameLevel = tr.find_all('td')[2].find('em').text.strip()
    killDeath = tr.find_all('td')[5].find('b').text.strip()
    winPercent = tr.find_all('td')[6].find('b').text.strip()
    timePlayed = tr.find_all('td')[7].text.strip()
    print(place, skillRating, gameLevel, killDeath, winPercent, percent, timePlayed )
    f.write(place + ","  + skillRating + "," + gameLevel + "," + killDeath + "," + winPercent + " % ," + timePlayed + "\n")         #write results to products.csv

f.close()
