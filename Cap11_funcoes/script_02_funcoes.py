
# definindo
def nnome_da_fucncao():
    pass

def nomeDaFuncao():
    pass

# chamar/executar
nomeDaFuncao()

# Saidas print/return/yield
def calcula_imc():
    peso = 84
    altura = 1.74
    imc = peso / altura ** 2
    print(f'IMC: {imc:.2f}')   ## <=== print como saída

calcula_imc()


def calcula_imc_2():
    peso = 94
    altura = 1.84
    imc = peso / altura ** 2
    return imc  ###<<=== return como saída


fabio_imc = calcula_imc_2()
print(fabio_imc)
print()

"""Documentar as funções """
# __DOCSTRINGS__

def calcula_imc_3():
    """Essa funcao realiza o calculo de Indice de Mass Corporal de apenas um individuo por vez"""
    peso = 95
    return peso

print(calcula_imc_3())
print(calcula_imc_3.__doc__)
print()

# Escopo de variaveis
# global <<== acessada em  qq parte do codigo
# local <<== dentro das funcoes

peso = 80

def calcula_imc_4():
    global peso
    peso = 84
    altura =1.74
    imc = peso/altura**2
    print(f'Valore da variavel peso DENTRO da funcao: {peso}') # << local (TENTEM USAR LOCAIS)
    return imc

calcula_imc_4()
print(f'Valore da variavel peso FORA da funcao: {peso}') # << global
print()

"""Argumentos de uma funcao"""
# Args requeridos

def calcula_imc_5(peso, altura):
    imc = peso/altura **2
    imc = f'{imc:.2f}'
    return imc

print(f'IMC de Fabio: {calcula_imc_5(84, 1.74)}')
print(f'IMC de Gabriel: {calcula_imc_5(74, 1.74)}')
print(f'IMC de Norton: {calcula_imc_5(84, 1.84)}')
print()

# Args padrao

def calcula_imc_6(peso=74, altura=1.74):
    imc = peso/altura **2
    return imc

print(calcula_imc_6(84))
print(calcula_imc_6(74, 1.80))
print(calcula_imc_6())  # sem paramentros funciona
print(calcula_imc_6(peso=60, altura=1.80)) ###<<< mais correta
print()
# Args tamanho vairavel - *args - tupla
def calcula_imc_7(*args):
    nome =args[0]
    peso =args[1]
    altura =args[2]

    # print(f'Argumentos passados na funcao: {args}')
    # print(f'Nome : {nome}')
    # print(f'IMC de {nome}: {peso/altura**2}')
    imc = peso/altura**2
    dados_paciente = [nome, peso, altura,imc]
    return dados_paciente

print(calcula_imc_7('Fabio', 84, 1.74, 45,'0464646464'))
print(calcula_imc_7('Norton', 74, 1.74))


# Args de palavra chave- **kwargs <<dicionario chave/valor
def calcula_imc_8(**kwargs):
    print(f'Kwargs passados: {kwargs}')
    nome = kwargs['nome']
    peso = kwargs['peso']
    altura = kwargs['altura']
    imc = peso / altura** 2
    dados_do_paciente = [nome, peso, altura, imc]
    return dados_do_paciente


print(calcula_imc_8(nome='Fabio', peso=84, altura=1.74))

"""Ordem dos argumntos"""
# requeiridos
# padrao
# *args
# **kwargs

def calcula_imc_9(nome, idade=40, *args, **kwargs):
    print(nome)
    print(idade)
    print(args)
    print(kwargs)

calcula_imc_9('Fabio', 44, 84, 1.74, cpf='0000000', idt='99999999')