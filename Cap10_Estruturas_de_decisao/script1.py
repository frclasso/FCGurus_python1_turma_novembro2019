

# if
# nome = input('Digite seu nome: ')
# if nome == 'Fabio':
#     print(f'Boa noite {nome}')


# if/else
# nome = input('Digite seu nome: ')
# if nome == 'Fabio':
#     print(f'Boa noite {nome}')
# else:
#     print('Usuario desconhecido...')

# elif
# switch-case
#opcao = input('Digite uma opcao: ')
# if opcao == '1':
#     print('Voce escolheu o produto 1')
# elif opcao == '2':
#     print('Voce escolheu o produto 2')
# elif opcao == '3':
#     print('Voce escolheu o produto 3')
# elif opcao == '4':
#     print('Voce escolheu o produto 4')
# else:
#     print('Opcao inexistente, voce precisa escolher uma opcao de 1 a 4')
#
#

# if aninhados
numero = int(input('Digite um numero: '))
if numero % 2 == 0:
    if numero % 3 == 0:
        print('Numeor divisivel por 2 e 3')
    else:
        print('Numero divisivel apenas por 2')
else:
    if numero % 3 == 0:
        print('Numero divisiel por 3 e nao por 2')
    else:
        print('Numero nao é divisivel nem por 2 nem por 3')