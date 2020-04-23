from datetime import datetime

now = datetime.now()
print(now)

data = now.date()
print(f'Data: {data}')

ano = now.year
print(f'Ano: {ano}')

mes = now.month
print(f'Mes: {mes}')

dia = now.day
print(f'Dia: {dia}')

hora = now.hour
print(f'Hora: {hora}')

minuto= now.minute
print(f'Minutos: {minuto}')

segs = now.second
print(f'Segundos: {segs}')