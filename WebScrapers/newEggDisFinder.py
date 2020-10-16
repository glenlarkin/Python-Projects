#! python3
#newEggDisFinder - Scrapes NewEgg.com for featured deals on monitors that Glen wants

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?N=100898493%20600417886%20600107132&PageSize=96&Order=1'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"           # creates .csv file named products
f = open(filename, "w")             # opens file for input

headers = "brand, product_name, price, shipping\n"             # table Head dividers

f.write(headers)

for container in containers:
        # brand = container.div.div.a.img["title"]                       # finds product brand in an <a> named title

         #title_container = container.find("a", {"class":"item-info"})                 #finds product_name in <a>
         #product_name = title_container.text.strip()

         price_container = container.findAll("li", {"class":"price-current"})             # finds price in <li>
         price = price_container[0].text.strip()                                                   # formats to price only

         shipping_container = container.findAll("li", {"class":"price-ship"})             # finds shipping price in <li>
         shipping = shipping_container[0].text.strip()                                             # formats to price only

        # print("brand: " + brand)                                                                           # shows results on Console
         #print("product_name: " + product_name)
         print("price: " + price)
         print("shipping: " + shipping)

         f.write(price + "," + shipping + "\n")         #write results to products.csv

f.close()                  #close file
