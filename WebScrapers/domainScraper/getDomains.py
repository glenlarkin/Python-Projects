import urllib
import csv
import re
from bs4 import BeautifulSoup
import requests

with open('WebScrapers/domainScraper/needed-emails-from-these-domains.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    newList=list(reader)
    #print(newList.count(newList))
    #print(newList)
    output = ''


    for column in newList:
        
        for query in column:
            query = query.replace(' ', '+')
            url = "https://google.com/search?q="+query
            #print(url)

            # Getting the webpage, creating a Response object.
            response = requests.get(url)

            # Extracting the source code of the page.
            data = response.text

            # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
            soup = BeautifulSoup(data, 'lxml')

            # Extracting all the <a> tags into a list.
            tags = soup.find_all('a')
            hrefs = tags.find_all('href', limit=3)
            print(hrefs)