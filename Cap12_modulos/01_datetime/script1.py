
import time

ticks = time.time()
print(f"Number of ticks since 12:00am January, 1, 1970: {ticks}")

# local time
print(time.localtime())
t1 = time.localtime()
ano = t1[0]
print(f'Ano: {ano}')

mes = t1[1]
print(f'Mes: {mes}')

dia = t1[2]
print(f'Dia: {dia}')

hora = t1[3]
print(f'Hora: {hora}')

minuto = t1[4]
print(f'Minuto: {minuto}')

segundo = t1[5]
print(f'Segundos: {segundo}')