

# finally
try:
    fh = open('clientes.csv', 'w')
    fh.write('Testando 123..')
    fh.close()
except FileNotFoundError:
    print('Arquivo nao econtrado')
finally:
    print('Fechando o arquivo')
