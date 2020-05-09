import zipfile
import os


def gera_arquivo_zipado():
    for root, subdir, files in os.walk('zips'):
        # print(files)
        for file in files:
            with zipfile.ZipFile('zipados.zip', 'a') as file_zip:
                caminho = f'{root}/{file}'
                print(caminho)
                file_zip.write(caminho)


#gera_arquivo_zipado()

# Ler o arquivos txt dentro  zipados.zip
my_zips = zipfile.ZipFile('zipados.zip', 'r')
for z in my_zips.namelist():
    print(z)
print()

# imprimir os metadados
for meta in my_zips.infolist():
    print(meta)
#
# print()
cars_info = my_zips.getinfo('zips/cars.txt')
print(cars_info)

# print(my_zips.read('zips/techBrands.txt'))
with my_zips.open('zips/techBrands.txt') as file:
    print(file.read())
#
# my_zips.extract('zips/techBrands.txt')
my_zips.extractall('.')