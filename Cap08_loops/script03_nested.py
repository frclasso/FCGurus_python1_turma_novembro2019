
# loop dentro de outro
#loops aninhados

carros = [
    [
        ['Tesla', 'Audi','Ferrari','Lamborghini'],
        ['BMW', 'VW','GMC'],
        ['Ford', 'Fiat','Porsche'],
    ]
]
#print(carros)
# print(carros[0])
# print(carros[0][0])
# print(carros[0][1])
# print(carros[0][2])
# print(carros[0][0][0])
for l1 in carros:
    for l2 in l1:
        for l3 in l2:
            print(l3)