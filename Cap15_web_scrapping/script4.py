import requests

url_xls = 'https://f001.backblazeb2.com/file/Datasets-gurus/xlsx_files/fruit_stores.xlsx'


response = requests.get(url_xls)
try:
    if response.status_code == 200:
        with open('fruits_local.xlsx', 'wb') as xls_writer:
            print(response.text.encode(encoding='utf-8'))
            xls_writer.write(response.content)
except Exception:
    print('Arquivo nao encontrado')


