import requests
import csv
# ler .csv da internet

url = 'https://f001.backblazeb2.com/file/Datasets-gurus/csv_files/arquivos_csv_pequenos/baby_names.csv'
response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.encoding)
with open('baby_names_local.csv', 'w', newline='') as csv_file_writer:
    for names in response.content.decode('utf-8'):
        #print(names, end='')

        """Error"""
        writer = csv.writer(csv_file_writer, delimiter=' ')
        writer.writerow(names.split())