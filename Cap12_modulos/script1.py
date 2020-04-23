# absoluto
import datetime

print(dir(datetime))

agora = datetime.datetime.now()
print(agora)

# relativo
from datetime import date

data =date.today()
print(data)


from gera_email import email_funcional


email = email_funcional('Fabio', 'Clsso', 'Nexxera')
print(email)