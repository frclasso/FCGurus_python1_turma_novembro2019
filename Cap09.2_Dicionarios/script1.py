
# dicionario vazio
aluno = {}
print(type(aluno))
print(len(aluno))

"""Adicionar elementos"""

aluno_1 = {'id' :1223, 'nome' :'Fabio' ,'sobrenome' :'Classo' ,'idade' :45 ,'curso' :'Sistema de informacao', 'turno' :'noturno'}

aluno_1['matricula'] = 3456789 #####

print(aluno_1)


"""Atualizar elementos"""
aluno_1['turno'] = 'vespertino' ### atualizando
print(aluno_1)

# update
aluno_1.update({'curso' :'Ciencias da computacao'}) ### atualizando
print(aluno_1)

aluno_1.update({'unidade_escolar' :'Florianopolis - Centro'})  ##### adicionando
print(aluno_1)

"""Remover elementos"""
#  __delitem__
aluno_1.__delitem__('idade')
print(aluno_1)

# pop
aluno_1.pop('matricula')
print(aluno_1)

# del
del aluno_1['sobrenome']
print(aluno_1)

# clear
# aluno_1.clear()
# print(aluno_1)
#
# del aluno_1
# print(aluno_1)

# keys , values, items
print(aluno_1.keys())
print(aluno_1.values())
print(aluno_1.items())


# funcao dict()
aluno_2 = dict(nome='Giovanna', idade=7, turno='matutino', unidade_educacional='Florianopolis -  Centro')
print(aluno_2)

for k, v in aluno_2.items():
    print(k, v)
print()

# zip
header = ['nome', 'idade', 'turno', 'unidade_educacional']
aluno_3 = ['Erick', 11, 'matutino', 'Centro']
erick ={}
for k,v in zip(header, aluno_3):
    erick[k] =v
print(erick)

#copiar
aluno_4 = aluno_2
print(aluno_4)
print(id(aluno_2))
print(id(aluno_4))
aluno_4['nome'] = 'Pedro'
print(aluno_2)

# certo
aluno_5= aluno_2.copy()
print(aluno_5)
aluno_5['nome'] = 'Jose'
print(aluno_2)
print(aluno_5)

# chaves inexiste
#print(aluno_5['telefone'])

# get()
print(aluno_5.get('telefone', 'Essa chave nao existe'))

# setdefault()
# idade, turno, unidade_escolar
aluno_6 = {'nome':'Fernanda'}
aluno_6.setdefault('idade',30)
aluno_6.setdefault('turno','diurno')
aluno_6.setdefault('unidade_escolar','Coqueiros')

print(aluno_6)


## criar um dict, sem valores
# fromkeys()
chaves = ['nome', 'idade','turno', 'unidade_escolar']
novo_aluno = dict.fromkeys(chaves)
print(novo_aluno)


# ordenacao
print(sorted(aluno_6))
print(sorted(aluno_6.items()))
#
# def ordena(aluno_x):
#     return aluno_x.nome
#
# print(sorted(aluno_6, key=ordena))

print()
print()
print()
print()

dicionario_aninhado = {
    'dict_a':{'key_1':'value_1'},
    'dict_b':{'key_2':'value_2'},
                        }
print(type(dicionario_aninhado))
print(dicionario_aninhado.keys())
print(dicionario_aninhado['dict_a'])
print(dicionario_aninhado['dict_b'])
print(dicionario_aninhado['dict_a']['key_1'])

aluno_7 = {'nome':'Fabio', 'idade':40, 'nome':'Jose'}
print(aluno_7)

# aluno_7 = dict(nome='Fabio', idade=40, nome='Jose')
# # print(aluno_7)