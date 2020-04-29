import os

# criar um diretorio
# if not os.path:
#     os.mkdir('teste_dir')
# print(os.listdir('.'))

# mudar de diretorio
os.chdir('teste_dir')
print(f'Diretorio atual: ', os.getcwd())
#print(os.listdir())

# voltar
os.chdir('../')
print(f'Diretorio atual: ', os.getcwd())

# deleter o teste_dir
os.rmdir('teste_dir')
print(f'Diretorio atual: ', os.getcwd())
print(os.listdir())