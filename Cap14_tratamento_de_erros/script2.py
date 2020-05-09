
try:
    a = int(input('Digite primeiro numero: '))
    b = int(input('Digite segundo numero: '))
    print('{} /{} = {}'.format(a, b, a/b))
except Exception as e:
    print("Erro desconhecido", e)
else:
    print('Deu certo')



# try:
#     a = int(input('Digite primeiro numero: '))
#     b = int(input('Digite segundo numero: '))
#     print('{} /{} = {}'.format(a, b, a/b))
# except ZeroDivisionError as e :
#     print("Nao é permitida divisao por zero ==>", e)
# except ValueError as e:
#     print('Valor invalido ==> ', e)