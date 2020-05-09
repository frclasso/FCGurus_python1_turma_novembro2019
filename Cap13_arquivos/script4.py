
# next() = recupera o propximo item do objeto iteravel

techs = open('tecnologias.txt', 'r')
print(f'Nome do arquivo: {techs.name}')


# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# print(next(techs))
# 10
#
for indice in range(3):
    t = next(techs)
    print(f'{indice} ==> {t}', end='')

techs.close()