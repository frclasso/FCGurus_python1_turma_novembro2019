
# lista vazia
disciplinas = []
print(type(disciplinas))
print(len(disciplinas))
print()

"""Adicionar elementos"""
# append
disciplinas.append('Fisica')

# insert
disciplinas.insert(0, 'Quimica')

# Usando extends
outras_disciplinas = ['Farmacologia', 'Estatistica', 'Matematica', 'Geologia', 'Economia']

#disciplinas.append(outras_disciplinas)
disciplinas.extend(outras_disciplinas)

"""Atualizar elementos"""
disciplinas[0] = 'Geografia'
print(disciplinas)

"""Deletar elementos"""
disciplinas.pop() # remove o ultimo elemento
print(disciplinas)

disciplinas.pop(0)
print(disciplinas)

#del
del disciplinas[0]
print(disciplinas)

#remove
disciplinas.remove('Geologia')
print(disciplinas)

# remover todos os valores
#print(disciplinas.clear())

# del disciplinas
# print(disciplinas)

# copiar listas

new_disciplinas = disciplinas

print(new_disciplinas)
new_disciplinas.append('Economia')

print(new_disciplinas)
print(id(new_disciplinas))

print(disciplinas)
print(id(disciplinas))
print()

new_disciplinas_2 = disciplinas[:]
#print(new_disciplinas_2)
new_disciplinas_2.append('Biologia')
print(new_disciplinas_2)
print(disciplinas)

# copy
new_disciplinas_3 = new_disciplinas_2.copy()
print(new_disciplinas_3)
print(id(new_disciplinas_3))
print()

# ordenar
# sort
new_disciplinas_3.sort(reverse=True)
print(new_disciplinas_3)

#sorted
tech_disciplinas = ['Sistemas de informacao', 'Ciencias da Computacao', 'Biotecnologia', 'Genetica', 'Genetica']
print(sorted(tech_disciplinas, reverse=True))
tech2 = sorted(tech_disciplinas)
print(tech2)

# reverse
tech_disciplinas.reverse()
print(f'Reverse: ',tech_disciplinas)

# contar elementos
print(tech_disciplinas.count('Genetica'))

# somar valores
valores = [230, 40, 50]
print(valores[0]+valores[1]+valores[2])
print(sum(valores))

# membership
print('Sistemas de informacao' in tech_disciplinas)
print('SISTEMAS DE INFORMACAO' in tech_disciplinas)


# classe list()
texto = 'Python Program language'
texto_para_lista = list(texto)
print(texto_para_lista)
texto_para_lista_2 = texto.split()
print(texto_para_lista_2)


# loops
l1= ['audi', 'bmw', 'vw']
l2 = ['ford', 'jeep', 'gmc']

companies = l1 + l2
print(companies)

companies_2 = []
for k, v in zip(l1, l2):
    companies_2.append(k)
    companies_2.append(v)
print(companies_2)
