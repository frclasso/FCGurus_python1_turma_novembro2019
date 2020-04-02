
# loop infinito
# while True:
#     print('Voce foi hackeado !!!!')

password = 'swordfish'

senha = input('Digite sua senha: ')

autorizado = False
count = 0
max_tentativas = 3

while password != senha:
    print('Senha incorreta')
    count += 1

    if count > max_tentativas:
        break
    senha = input('Digite sua senha: ')
    print('Not allowed.')
else:
    autorizado = True
    print('Login ok')
