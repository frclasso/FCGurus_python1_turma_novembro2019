from collections import namedtuple

# Namedtuple()

Person = namedtuple('Person', 'nome sobrenome cep')
p1 = Person('Fabio', 'Classo', 88034345)
print(type(p1))
print("Nome: {}, Sobrenome: {}, CEP: {}".format(p1.nome, p1.sobrenome, p1.cep))
print("Nome: {}, Sobrenome: {}, CEP: {}".format(p1[0], p1[1], p1[2]))
print(f'Campos: {p1._fields}') # semelahante ao keys.() de dicionarios

p2 = p1._replace(cep=88034350)
print(p2)

#convertendo em dicionario
print(p2._asdict())

# Criar uma namedtuple a partir de um dicionarios
john_doe = {'nome': 'John', 'sobrenome':'Done', 'cep':'000000'}
john = Person._make(john_doe.values())
print(john)