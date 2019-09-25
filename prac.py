from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')
quotes = page_soup.findAll('div', {'class': 'quotes'})


for quote in quotes:
    fave_quotes = page_soup.findAll('p', {'class': 'aquote'})
    aquote = fave_quotes[0].text.strip()

    fave_authors = page_soup.findAll('p', {'class': 'author'})
    author = fave_authors[0].text.strip()

    print(aquote)
    print(author)
