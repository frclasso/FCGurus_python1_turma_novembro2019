import calendar

calendario = calendar
print(dir(calendario))


print(calendario.month(2020, 4))

print()
print()
print()  # 1 = espacameto
         # 3 - espcamento entre calendarios do mes
         # 4 quantidade exibida
         
# print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2020, 2,1,3 ,4))

# anos bisextos
print(calendar.isleap(1999))
print(calendar.isleap(2000))

ano = 2000
if calendar.isleap(ano):
    print(f'Ano Bisexto: {ano}')
else:
    print('Nao é ano bisexto.')


"""
    CRIAR UMA FUNCAO QUE RECEBE UM ANO, VERIFICA SE ELE EH BISEXTO, E SE FOR
    RETORNA O CALENDARIO DO MESMO.
"""