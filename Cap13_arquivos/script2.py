
fabio = {'nome':'Fabio',
         'sobrenome':'Classo',
         'nacionalidade':'Brasileiro',
         'estado_civil':'solteiro',
         'formacao':'Sistemas de Informacao'}

print(fabio)
arquivo = open('my_clients.txt', 'a') #w
arquivo.write('Dados de clientes')
arquivo.write('\n')

for k, v in fabio.items():
    arquivo.write(k + ':' + v + '\n')

arquivo.close()