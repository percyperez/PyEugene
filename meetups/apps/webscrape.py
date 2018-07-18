import bs4
import csv
import requests
import sys

url = "http://planetpython.org"
source = requests.get(url)

soup = bs4.BeautifulSoup(source.content, 'lxml')


def get_content():
    links = [link.get('href') for link in soup.find_all('a')]

    return links


def content_to_csv():
    writer = csv.writer(sys.stdout)
    links = get_content()
    writer.writerow(['Link'])
    for link in links:
        writer.writerow([link])
    writer.writerow([])
