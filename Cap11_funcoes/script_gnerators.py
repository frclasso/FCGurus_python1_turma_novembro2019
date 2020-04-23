

def numeros():
    for i in range(10):
        #print(i)
        return i

# print(numeros())

def gen_nums():
    for i in range(10):
        yield i

numeros_l = []

for numbers in gen_nums():
    # print(numbers)
    numeros_l.append(numbers)

print(numeros_l)
n = iter(numeros_l)
#print(n)
print(next(n))
print(next(n))
print(next(n))
print(next(n))