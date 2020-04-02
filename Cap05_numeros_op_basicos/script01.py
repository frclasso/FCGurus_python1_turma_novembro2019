print(type(3))
print(type(3.14159))
print(type(3+2j))

print(float(3))
print(int(3.14159))

# Adicao, sub, multiplicao

# Modulo, retorna o resto de uma divisao
print(f'10 % 3 = {10 % 3}')

# Divisao real /
print(f'10 / 3 = {10 / 3}')

# Divisao inteira //
print(f'10 // 3 = {10 // 3}')

# exponencial
print(f'3 ** 2= {3 ** 2}')

# precendencia
print(2**2 * 4)

## Op comparacao
a = 21
b = 10

print(f'a == b: {a == b}')
print(f'a != b: {a != b}')
print(f'a > b: {a > b}')
print(f'a < b: {a < b}')
print(f'a <= b: {a <= b}')
print(f'a >= b: {a >= b}')

# Op Atribuicao
c = 0

# add and  +=
a += 1  # Python 3.5
print(a)
a = a + 1
print(a)

# sub and -=
a -= 1
print(a)
a = a - 1
print(a)

# mult and *=
a *= 2
print(a)
a = a * 2
print(a)

# divide and /=
a /=2
print(a)
a = a / 2
print(a)

# exp and **=
a **= 2
print(a)
a = a ** 2
print(a)

# modulo and
print(b)
#b %= 3
b = b % 3
print(b)

# flor and //=
c = 10
#c //= 3
c  = c // 3
print(c)
print()

# Op logicos
p = True
q = False

# conjuncao AND (basta ter 1 false, retorna False)
print(p and q)
print(p and p)
print(p and True)
print(p & True)
print(q & q)
print()

# Disjuncao OR (basta em True, retorna True)
print(p or q)
print(p | q) # pipe
print(p or False)
print(p or p)
print(q or q)
print()

# Negacao
print(not p)
print(not q)
print(not True)
print(not False)
print()
print(not 0)
print(not 1)

# Bitwise Ops
a = 60
b = 13
print("a  em binario: : ", format(a, '08b'))
print("b  em binario: : ", format(b, '08b'))

# and
print("a AND b:         ", format(a & b, '08b'))

#or
print("a OR b:          ", format(a | b, '08b'))

#not
print(a)
print(~a)
print("NOT a:           ", format(~a, '08b'))
#right
print("a << 2:          ", format(a << 2, '08b'))
print(a << 2)

#left
print(a)
print("a >> 2:          ", format(a >> 2, '08b'))
print(a >> 2)