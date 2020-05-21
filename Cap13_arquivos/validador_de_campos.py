import os
# print(os.listdir())

from clientes_autalizado import cabecalho, clientes

# print(cabecalho)
# print(clientes)

# ATIVIDADE DA SEMANA
# 1 - criar uma funcao que valide email "nome.sobrenome@empresa.com"
 # criar lista de empresas
# 2 - criar uma funcao que valide telefone, remover caracteres que nao sejam numeros
# 3 - criar uma funcao que valide data:  "2010-01-05"
# 4 - criar uma funcao que leia  o coteudo da lista cientes

clientes_iter = iter(clientes)


def get_uma_linha():
    """Retorna o conteudo de uma linha"""
    cliente = []
    for i in range(8):
        #print(next(clientes_iter))
        dados = next(clientes_iter)
        cliente.append(dados)
    return cliente


linha = get_uma_linha()


def gera_email(line):
    """Retorna o email de um cliente"""
    # print(linha)
    # print(linha[0])
    nome_completo = linha[0]
    nome, sobrenome = nome_completo.split()
    # print(nome)
    # print(sobrenome)
    email = f"{nome.lower()}.{sobrenome.lower()}@email.com"
    # print(email)
    return email


def valida_telefone(linha):
    telefone = linha[4]
    # print(telefone)
    telefone = telefone.replace('(', '').replace(")", '').replace('-','')
    #print(telefone)
    return telefone



def valida_data(linha):
    data = linha[7]
    ##print(data)
    data = data[:10]
    #print(data)
    return data



def cliente_autalizado(linha):
    # print(linha)
    email = gera_email(linha)
    telefone = valida_telefone(linha)
    data = valida_data(linha)

    dados_atualiazdos = linha
    dados_atualiazdos.pop(3)
    dados_atualiazdos.insert(3, email)

    dados_atualiazdos.pop(4)
    dados_atualiazdos.insert(4, telefone)

    dados_atualiazdos.pop(7)
    #print(data)
    dados_atualiazdos.insert(7, data)

    return dados_atualiazdos

import csv

with open('clientes_autalizados.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for c in clientes:
        try:
            linha = get_uma_linha()
            c = cliente_autalizado(linha)
            writer.writerow(c)
            #print(c)
        except StopIteration:
            break
