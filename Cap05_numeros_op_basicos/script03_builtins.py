
# Built in
# dir()
print(dir())
print()

# built_ins
#print(dir('__builtins__'))

# help
#print(help(list))

# type
print(type('Pyhton'))

#id
nome = 'Python'
print(id(nome))

input
# lang = input('Digite sua linguagem favorita: ') # string
# versao = float(input('Digite a versao: '))
# ano = int(input('Digite ano: '))
#
# print(lang)
# print(versao)
# print(ano)

# isistance - parecido com type
companies = ('Audi', 'Tesla', 'VW')
print(isinstance(companies, tuple))

# len, tamanho ou qtd de elementos
print(len(companies))
print(len('Python'))
print()

#range - intervalo
print(range(10))
print(list(range(10)))

# start, stop
print(list(range(5,50)))

# start, stop, step
print(list(range(0,51,5)))

# round
print(round(3.12149382984, 5))
print(round(6.5, 2))


# abs
print(abs(-123))

# pow - exponencial
print(pow(3, 2))
print(3 ** 2)

# sorted
nums = [-1,-2,-3,0,3,2,1,10,-10]
print(sorted(nums))
print(sorted(nums,reverse=True))

nomes = ['Carolina', 'Ana', 'Giovanna']
print(sorted(nomes))

# enumarete
print(list(enumerate('Python')))
for n, v in enumerate(nomes):
    print(n, v)