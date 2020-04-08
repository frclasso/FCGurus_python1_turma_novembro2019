
#
empty_string = ''
print(type(empty_string))
print(len(empty_string))

my_string = 'Floripa Code Gurus escola de tecnologia'
# index
print(my_string[0])
print(my_string[-1])

#slicing
print(my_string[:7])
print(my_string[29:])

#concatenacao
new_string = 'Django e Python'
print(my_string + ' ' + new_string)
new_string2 = my_string + ' ' + new_string
print(new_string2)
print(len(new_string2))
n3 = new_string2[:49] + 'Ruby'
print(n3)

# print(dir(str))

# in not in
print('Django' in n3)
print('Python' not in n3)

# Max
print(max('abcbdefghijz'))
print(max('ABCDBFGEabcbdefghijz'))
print(max(10, 20))

#Min
print(min('abcbdefghijz'))
print(min('ABCDBFGEabcbdefghijz'))
print(min(10, 20))

#metodos da classe str
print(my_string)
print(my_string.upper()) # retorna maiusculo
print(my_string.lower()) # retorna minusculo
print(my_string.capitalize()) # retorna primeira letra maiuscula
print(my_string.title()) # retorna letra de cada palavra maiusculala
print(my_string.swapcase()) # inverte o case
print()

# split
print(my_string)
# l = []
# # l.append(my_string[0:7])
# # l.append(my_string[7:12])
# # l.append(my_string[12:18])
# # print(l)
l2 = my_string.split()
print(l2)

# join - junta
l3 = ' '.join(l2)
print(l3)

# strip
frase = "**** *Floripa Code Gurus Esco**la de Tecnologia *** *** "
print(frase.strip('*').strip(' * '))

# index
print(frase.index('Gurus'))

# find
palavra = 'Gurus'
print(frase.find(palavra))

# replace
print(frase.replace('Tecnologia', 'Technology'))
print(frase.replace('*', ''))

# count
print(frase.count('Floripa'))
print(frase.count('Gurus'))
print(frase.count('o'))

#startswith
for caracter in frase:
    if caracter.startswith('E'):
        print(frase.index(caracter))
#endswith
print('Python'.endswith('n'))

# zfill
print('45'.zfill(5))

print()