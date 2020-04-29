

# asctime() - converte um tupla de structtime valores  no formato Ter 28 fev hora 2020.


import time

t1 = time.localtime()
print(t1)
t2 = time.asctime(t1)
print(t2)