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
        print(column)
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
            tags = soup('a', href=True)
            
            # Extracting URLs from the attribute href in the <a> tags.
            for tag in tags:
                result = tag.get('href').strip('/url?=q')

                #y = tag.findall(r'(https?://\S+)', result)
                print(result.strip())
                #print(result)
                

            with open ('test1.csv', 'a', newline='') as fout:
                cw = csv.writer(fout)
                for result in column:
                    
                    cw.writerow([query])
                    #print(query)