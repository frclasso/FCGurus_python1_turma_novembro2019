

# Op associacao
# in e not in
tecnlogias = ['Python', 'Django', 'Ruby', 'Flask']

print('Python' in tecnlogias)
print('Python' not in tecnlogias)
print('Java' not in tecnlogias)
####
print('Py' in tecnlogias)
python = tecnlogias[0]
print('Py' in python)

print()
for tech in tecnlogias:
    if tech == 'Python':
        print('Welcome the Python world')
    else:pass

# Op identidade
# is e is not
x = 100
print(id(x))
y = 100.0
print(id(y))
print(x is y)
print(x is not y)
z = x
print(z is x)
print(id(z))
a = 100
print(a is x)
print(id(a))