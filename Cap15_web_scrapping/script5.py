import requests

url_img = 'https://f001.backblazeb2.com/file/Datasets-gurus/imagens_download/aguia+-+natureza+selvagem+-+%232.jpg'
response = requests.get(url_img)
print(response.status_code)
print(response.content)
with open('figura.jpg', 'wb') as img_writer:
    img_writer.write(response.content)

