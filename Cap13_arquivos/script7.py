import datetime

# gerar um .csv

headers = ['nome', 'sobrenome', 'idade', 'cpf', 'email', 'fone', 'formacao', 'criado_em']

criado_em = datetime.date.today()

cliente1 = [
    'Fabio', 'Classo', '45', '000000000', 'fabioclasso@nexxera.com', '(48)9999999',
    'Sistemas de informcao', str(criado_em)
]
cliente2 = [
    'John', 'Doe', '45', '000000000', 'fabioclasso@nexxera.com', '(48)9999999',
    'Sistemas de informcao', str(criado_em)
]

# Caso 1
with open('clientes.csv', 'w') as file:
    for header in headers:
        file.write(header + ',')
    file.write('\n')
    for cliente in cliente1:
        file.write(cliente + ',')


# Caso 2
import csv

with open('clientes.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(headers)
    writer.writerow(cliente1)
    writer.writerow(cliente2)
