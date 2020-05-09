

arquivo_reader = open('my_clients.txt', 'r')

# for data in arquivo_reader:
#     print(data, end='')


# cursor
# tell()
print(f'Lendo o arquivo: {arquivo_reader.read(18)}')
print(f'Posicao atual do cursor: {arquivo_reader.tell()}')

# modificar a posicao do cursor
cursor = arquivo_reader.seek(0)
print(f'Posicao atual do cursor: {arquivo_reader.tell()}')
print(f'Lendo o arquivo: {arquivo_reader.read(18)}')
