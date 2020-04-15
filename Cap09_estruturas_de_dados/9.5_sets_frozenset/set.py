# set {}

# vazio

cursos = ()
print(type(cursos))

curso_2 = {}
print(type(curso_2))

curso_3 = set()
print(type(curso_3))

cs_cursos = {'Historia', 'Matematica', 'Fisica', 'Quimica', 'Arte', 'Fisica', 'Arte'}
print(cs_cursos)

# in e not in
print('Python' in cs_cursos)
print('Python' not in cs_cursos)

# adicionar elementos
cs_cursos.add('Big Data')
cs_cursos.add('Data Science')
cs_cursos.add('Data Science')
cs_cursos.add('Data Science')
cs_cursos.add('Data Science')
print(cs_cursos)

# remover
# pop
print(f'Removendo com pop(): {cs_cursos.pop()}')  #
print(cs_cursos)

# remove
# cs_cursos.remove('Data Science')
# print(cs_cursos)

# clear()
# cs_cursos.clear()
# print(cs_cursos)
print()
# Operacoes de conjuntos
art_courses = {'Desgin', 'Pintura', 'Musica', 'Arte'}
print(f"Intersecao: {cs_cursos.intersection(art_courses)}")
print(f"Diferenca: {cs_cursos.difference(art_courses)}")
print(f"Uniao: {cs_cursos.union(art_courses)}")

print()
print(f'Intersecao: {cs_cursos & art_courses}')
print(f'Diferenca: {cs_cursos - art_courses}')
print(f'Uniao: {cs_cursos | art_courses}')
