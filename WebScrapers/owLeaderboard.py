import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime

# get the data for Overwatch leaderboards
data = requests.get('https://overwatch.op.gg/leaderboards?platform=pc')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('table', { 'class': 'LeaderBoardsTable' })
tbody = leaderboard.find('tbody')

wb = Workbook()
workSheet = wb.active

# Table Headers
#workSheet['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'] = ['Postion', 'Skill Rating', 'Game Level', 'K:D Ratio', 'Win Percentage', 'Time Played']

#filename = "OverwatchLeaders.csv"           # creates .csv file named products
#f = open(filename, "w")             # opens file for input

headers = "Postion, Skill Rating, Game Level, K:D Ratio, Win Percentage, Time Played \n"             # table Head dividers
percent = '%'
#f.write(headers)

for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    username = tr.find_all('td')[2].find('b').text.strip()
    skillRating = tr.find_all('td')[3].text.strip()
    gameLevel = tr.find_all('td')[2].find('em').text.strip()
    killDeath = tr.find_all('td')[5].find('b').text.strip()
    winPercent = tr.find_all('td')[6].find('b').text.strip() + percent
    timePlayed = tr.find_all('td')[7].text.strip()
        # Show Results to console
    print(place, username, skillRating, gameLevel, killDeath, winPercent, timePlayed )
        # Update doc with scraped data
    workSheet.append([place, username, skillRating, gameLevel, killDeath, winPercent, timePlayed])
    #f.write(place + "," + skillRating + "," + gameLevel + "," + killDeath + "," + winPercent + " % ," + timePlayed + "\n")         #write results to products.csv

#f.close()

todayDate = datetime.datetime.today().strftime('%m/%d/%Y')
#wb.save("OWLeaders" + todayDate + ".xlsx")