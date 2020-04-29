import random


def gera_cpf_valido():
    """Essa funcao gera 1000 cpfs válidos com 11 algarismos"""
    lista_de_cpfs = []
    for i in range(1000):
        cpf = random.randint(10000000000, 19999999999)
        lista_de_cpfs.append(cpf)

    return lista_de_cpfs


for values in gera_cpf_valido():
    print(values)
