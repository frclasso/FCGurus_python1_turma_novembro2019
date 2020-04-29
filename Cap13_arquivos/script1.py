
"""
    Modos de escrita e leitua
    w = write ( insere conteudo no inicio do arquivo)
    r = read (le)
    a = append ( insere conteudo no final do arquivo)
    b = binario
    wb = escrita binaria
    rb = leitura binario
    wb+
    rb+
"""

arquivo = open('teste.txt', 'w')
print(arquivo.name)
arquivo.write('Python é minha linguagem favorita')
arquivo.write('\n')
arquivo.write('Python é minha linguagem favorita')
