import requests
import json


url_json = 'https://f001.backblazeb2.com/file/Datasets-gurus/json/a_movie.json'

response = requests.get(url_json)
try:
    if response.status_code == 200:
        print(response.text)
        f = open('movies.json', 'w')
        f.write(response.text)
except Exception:
    print('Arquivo nao encontrado')


with open('movies_2.json', 'w') as json_writer:
    data = json.loads(response.text)
    json.dump(data, json_writer, indent=1)