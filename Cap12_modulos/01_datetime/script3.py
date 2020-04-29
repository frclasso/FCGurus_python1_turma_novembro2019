from datetime import datetime

now = datetime.now()
print(now)

"""A funcao strftime() formatar os campos data e hora"""

"""
    Formatando dias:
    %a - nomes da semana abreviados: Mon, Tues, Wed
    %A - Monday, Tuesdya, Wednesday
    %d - dias em formato numerico: 10th of January 
"""
print(now.strftime("%a"))
print(now.strftime("%A"))
print(now.strftime("%d"))

"""
    Formatando meses
    %b - abreviados: Jan, Feb, Mar
    %B - nomes completos: January, February
    %m - representacao numerica: 01/01
"""

print(f"Mes: {now.strftime('%b')}")
print(f"Mes: {now.strftime('%B')}")
print(f"Mes: {now.strftime('%m')}")

"""
    Formatando ano:
    %y - ano abreviado - 2 algarismos
    %Y - ano completo - 4 algarismos
"""
print(f"Ano: {now.strftime('%y')}")
print(f"Ano: {now.strftime('%Y')}")
"""
    Formatando horas, minutos e segundos
    %H houras
    %M minutos
    %S segundos
    %p AM ou PM
"""
print(f'Hora/min/segundo: {now.strftime("%H")}')
print(f'Hora/min/segundo: {now.strftime("%M")}')
print(f'Hora/min/segundo: {now.strftime("%S")}')
print(f'Hora/min/segundo: {now.strftime("%p")}')

#juntar tudo
print(f'Today is {now.strftime("%B")} {now.strftime("%d")}, {now.strftime("%Y")}, '
      f'at time {now.strftime("%H:%M:%S %p")}.')