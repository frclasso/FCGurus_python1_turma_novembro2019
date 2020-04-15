
# set
numeros = {1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8}
print(type(numeros))
print(numeros)

# adicionar
numeros.add(1000)
print(numeros)

# frozenset
frozen_numeros = frozenset(numeros)
print(frozen_numeros)
print(type(frozen_numeros))

#frozen_numeros.add(1000)