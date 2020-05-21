import requests
from bs4 import BeautifulSoup

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
print(page.status_code)
# for header in page.headers:
#     print(header)
# for content in page.text:
#     print(content, end='')

print()
print()
print()
with open('simple.html', 'w') as html_writer:
    soup= BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    html_writer.write(str(soup))
print()

# for tags in list(soup.children):
#     print(tags)

# print(soup.find_all('p'))
# print(soup.find_all('p')[0].get_text())