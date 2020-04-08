

# Dados de clientes
cliente1 = ['Fabio', 'reis','CLASSO', '.111.222.333.444', '123456789', '(48)9999-8888']
cliente2 = ['Fabio', 'reis','CLASSO', '.111.222.333.444', '123456789', '(48)9999-8888']

nome = cliente1[0].upper()
sobrenome1 = cliente1[1].upper()
sobrenome2 = cliente1[2].upper()

print(nome,sobrenome1,sobrenome2)

cpf = cliente1[3]
print(cpf)
cpf_new = cpf.zfill(19)
print(cpf_new)

idt = cliente1[4].zfill(10)
print(idt)

####### FIXME
tel = cliente1[5]
for char in tel:
    if char in ['(', ')', '-']:
        print(tel.replace(char, ''))


# nome completo
nome_completo = nome +'.'+ sobrenome2
print(nome_completo)
# email
email = nome_completo.lower()+'@empresa.com'
print(email)

cliente1 = [nome_completo, cpf_new, idt, tel,email]
print(cliente1)


"""Atividade proposta"""

"""
 Copiem o conteúdo do arquivo: 00_snippets > clientes.csv
 
 em um arquivo Python criem uma lista clientes = [] e colem o conteúdo;
 
 1) Verificar se todos os CPFs são válidos ( se sao inteiros e com o tamanho padrão), corrija os inválidos;
 2) Verificar se todas as idades são válidas (se sao inteiras e dentro do limite "humano")
 https://pt.wikipedia.org/wiki/Lista_das_pessoas_mais_velhas_do_mundo, corrija os inválidos
 
 3) limpar os caracters do campo telefone "(" ")" "-", 
 
 4) Verificar se todos os email são válidos, corrija os inválidos
"""

# Dicas usar o script acima e script01.py deste capítulo
