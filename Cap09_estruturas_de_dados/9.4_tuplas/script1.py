

# tuplas
# tupla vazia
tupla_vazia  =()
print(f'Tipo: {type(tupla_vazia)}')

# tupla de um elemento
tupla_de_um_elemento = (50, )  # <====
print(f'Tipo: {type(tupla_de_um_elemento)}')

# ou
tupla_de_um_elemento_sem_parenteses = 50,
print(f'Tipo: {type(tupla_de_um_elemento_sem_parenteses)}')

# Acessando valores
cursos_1 = ('Matematica', 'Economia', 'Estatistica')
print(f'Retorna o valor relacionado ao indice "0" na tupla cursos_1: {cursos_1[0]}')

# indexar
print(f"Retorna o indice 'Econonomia' na tupla cursos_1: {cursos_1.index('Economia')}")

# concatenacao
cursos_2 = ('Quimica', 'Fisica', 'Biologia')
print(f"Concatenacao: {cursos_1+cursos_2}")
all_cursos = cursos_1 + cursos_2

# repeticao '*'
print(f"Repeticao: {cursos_2 * 3}")

# Iverter os valores
print(f"Invrtertido: {all_cursos[::-1]}")

# Ordenacao
print(f"Ordenando: {sorted(all_cursos,reverse=True)}")
print(f"Ordenando: {tuple(sorted(all_cursos,reverse=True))}")


# Op basicas (len, max, min, in , not in)
print(f"len() de all_cursos: {len(all_cursos)}")

nums = (100,30,4,25)
print(f"Max de nums: {max(nums)}")
print(f"Min de nums: {min(nums)}")

# in /not in
print(f"Verfica de Python esta em all_cursos: {'Python' in all_cursos}")
print(f"Verfica de Python NAO esta em all_cursos: {'Python' not in all_cursos}")

# LOOPS
print('Usando laço for')
for num, curso in enumerate(all_cursos, start=1):
    print(num, '==>',curso)
print()

# while
print('Usando laço While')
count = 0
while count < len(all_cursos):
    print(count + 1, "==>", all_cursos[count])
    count += 1
print()

# classe tuple()
lista_de_cursos = list(all_cursos)
print(type(lista_de_cursos))
print(lista_de_cursos)
all_cursos_t = tuple(lista_de_cursos)
print(type(all_cursos_t))
print()

# string
tec = 'Python'
t1 = tuple(tec)
print(t1)

## Imutabilidade
# pop, append, insert, del , remove - NAO FUNCIONAM EM TUPLAS
#all_cursos_t[0] = 'Python' # TypeError: 'tuple' object does not support item assignment

#all_cursos_t.pop() # AttributeError: 'tuple' object has no attribute 'pop'

#all_cursos_t.append('Django') #AttributeError: 'tuple' object has no attribute 'append'


all_cursos_t_2 = all_cursos_t[:1]
print(all_cursos_t_2)

## Util
usuario = ('id', 'username', 'password')
del usuario
print(usuario)
usuarios = [
    ('Fabio',),
    ('Gabriel'),
    ('Norton')
]

u = [
    {'fabio':('Fabio','Classo')},
    {'Gabriel':('demais dados',)}
]