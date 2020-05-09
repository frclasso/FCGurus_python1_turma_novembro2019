# gerenciador de conteudo

"""
    with open(nome do arquivo, modo de leitura) as apelido:
        bloco de operacoes...
"""

# ler

# read()
with open('my_clients.txt', 'r') as file:
    l = file.read(10)  # le conteudo inteiro do arquivos
    print(l)


# # readline() - primeira linha
# with open('my_clients.txt', 'r') as file:
#     l = file.readline()
#     print(l)


# readlines() - retorna uma lista de linhas
with open('my_clients.txt', 'r') as file:
    l = file.readlines(29)
    print(l)
