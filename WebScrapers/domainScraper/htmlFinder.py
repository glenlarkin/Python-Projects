from bs4 import BeautifulSoup
url = "https://"
soup = BeautifulSoup('url', 'url.parser')

url = "https://google.com/search?q="+query
            #print(url)

            # Getting the webpage, creating a Response object.
            response = requests.get(url)

            # Extracting the source code of the page.
            data = response.text

            # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
            soup = BeautifulSoup(data, 'lxml')

print(soup.prettify())