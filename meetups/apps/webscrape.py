import bs4
import requests

url = "http://planetpython.org"
source = requests.get(url)

soup = bs4.BeautifulSoup(source.content, 'lxml')

def get_content():
    links = [link.get('href') for link in soup.find_all('a')]

    return links
