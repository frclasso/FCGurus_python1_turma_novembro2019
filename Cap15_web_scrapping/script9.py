
from bs4 import BeautifulSoup

with open('books.xml', 'r') as file_reader:
    contents = file_reader.read()
    soup = BeautifulSoup(contents, 'lxml')
    titles = soup.find_all('title')
    authors = soup.find_all('author')
    price = soup.find_all('price')
    for i in range(0, len(titles)):
        print(titles[i].get_text(), end=', ')
        print(authors[i].get_text(), end=', ')
        print(price[i].get_text())
    print()