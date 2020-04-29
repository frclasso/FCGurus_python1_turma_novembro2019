import datetime

print(dir(datetime))

agora = datetime.datetime.now()
print(f'Agora: {agora}')

data_atual = datetime.date.today()
print(f'Data de hoje: {data_atual}')
print(f'Ano: {data_atual.year}')
print(f'Mes: {data_atual.month}')
print(f'Dia: {data_atual.day}')
print()

# passar argumentos data fixa/pre determinanda
my_date = datetime.datetime(2019, 9, 25, 12, 30, 45)
print(f'Data pré definida, ano: {my_date.year}')
print(f'Data pré definida, mes: {my_date.month}')
print(f'Data pré definida, dia: {my_date.day}')
print(f'Data pré definida, hora: {my_date.hour}')
print(f'Data pré definida, minutos: {my_date.minute}')
print(f'Data pré definida, segundos: {my_date.second}')
print()

# limpando caracteres
hoje = datetime.date.today()
print(f'Hoje: {hoje}')
print(type(hoje))
t1 = str(hoje).split('-')
print(t1)

hoje_atualizado = ''.join(t1)
print(hoje_atualizado)

t2 = str(hoje).replace('-', '')  # replace
print(t2)