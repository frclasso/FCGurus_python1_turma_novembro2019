
lang= 'Python'
def get_id(x):
    return id(x)

print(get_id(lang))

print((lambda x: id(x))(lang))

# identidade = lambda x: id(x)
# print(identidade(lang))

soma = lambda x, y: x + y
print(soma(4,5))
print()

print((lambda x: x + 3)(2))
"""
    o mesmo que lambda 2: 2 + 3
                           2 + 3
                             5
"""
# Argumentos
print(f'Soma com argumentos *args: {(lambda *args: sum(args))(20,30,50)}')

# Argumetos de palavras chaves
print(f'Soma com **kwargs: {(lambda **kwargs: sum(kwargs.values()))(primeiro=10, segundo=20, terceiro=30)}')

nome_completo = lambda nome, sobrenome: f'Nome completo: {nome.title()} {sobrenome.title()}'
print(nome_completo('fabio', 'CLASSO'))

email_funcional = lambda nome, sobrenome, empresa: nome.lower() + '.' + sobrenome.lower() +'@'+ \
                                                   empresa.lower() + '.com'

print(email_funcional('Fabio', 'CLASSO', 'neXXera'))