import requests


url = 'https://docs.python.org/'
response = requests.get(url)

print(response)
print(response.content)
with open('docs_python_org.html', 'w', encoding='utf-8') as file:
    for c in response.text:
        # print(c, end='')
        file.write(c)

