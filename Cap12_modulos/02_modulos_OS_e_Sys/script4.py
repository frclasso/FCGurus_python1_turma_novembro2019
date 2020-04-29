import os

# os.walk()
# for root, subdirs, files in os.walk('../'):
#     # print(f'Diretorio raiz: {root}')
#     # print(f'Diretorio raiz: {subdirs}')
#     # print(f'Diretorio raiz: {files}')
#
#     print(f'caminho completo: {root}{subdirs}{files}')

for root, subdirs, files in os.walk('.'):
    if files:
        print(files)

