import requests

url = 'https://f001.backblazeb2.com/file/Datasets-gurus/informacoes_tributarias.xml'

response = requests.get(url)
print(response.status_code)
print(response.headers)
print(response.encoding)

with open('info_trib_local.xml', 'w') as xml_writer:
    #for c in response.text:
    for c in response.content.decode('ISO-8859-1'):
        # print(c,end='')
        xml_writer.write(c)




# ISO-8859-1
# utf-8
# latin-1