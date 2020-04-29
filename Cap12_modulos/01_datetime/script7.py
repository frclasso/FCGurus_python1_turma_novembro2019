from datetime import datetime, timedelta

# situacao oo D-1
now = datetime.now().date()
print(now)

delta = timedelta(days=1)
ontem = now - delta
print(ontem)

data_futura = timedelta(days=7)
print(f'Daqui uma semana: {now + data_futura}')