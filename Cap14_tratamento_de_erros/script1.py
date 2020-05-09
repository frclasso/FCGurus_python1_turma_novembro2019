"""
    try:
        pass
    except:
        pass

"""
try:
    file = open('texte.txt', 'r')
    print(file.read())
except FileNotFoundError as erro:
    print('Arquivo nao encontrado ==>', erro)