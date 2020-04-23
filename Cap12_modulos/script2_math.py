import math
import random

# matematico e aleatorio
# math e random

PI = math.pi
print(PI)

# print(dir(math))

print(f'Seno de um numero: {math.sin(10)}')
print(f'Coseeno de um numero: {math.cos(10)}')
print(f'Tangente de um numero: {math.tan(10)}')
print(f'Raiz quadrada de um numero: {math.sqrt(12)}')
print()

# random
#print(dir(random))
print(random.random())  # um valor entre 0 e 1

# randrange
print(range(10))
vals = random.randrange(10, 20)
print(vals)

# choice
tecnologies = ['Pyhton', 'Django', 'Kivy', 'C++', 'Go']
print(random.choice(tecnologies))

# shuffle
cards = ['Jack', 'Queen', 'King', 'Ace']
random.shuffle(cards)
print(cards)

# sample
megaSena = random.sample(range(61), 6)
print(megaSena)