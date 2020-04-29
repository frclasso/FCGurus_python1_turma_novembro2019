import os

# multiplos sub diretorios
if not os.path:
    os.makedirs('temp/aula7/os/sys/arquivos')
else:
    print('Diretorio já existe')

print(os.listdir())