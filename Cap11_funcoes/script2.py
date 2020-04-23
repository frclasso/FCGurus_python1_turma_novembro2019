

pessoas = {
    1:{'nome':'John', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    2:{'nome':'Jane', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    3:{'nome':'Mary', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    4:{'nome':'Peter', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    5:{'nome':'Harry', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    6:{'nome':'Susan', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    7:{'nome':'Michael', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    8:{'nome':'Jimmy', 'sobrenome':'', 'idade':20, 'sex':'M'},
}

lista_de_emails = []
lista_de_sobrenomes = ['Lennon', 'Fonda', 'Jane','Parker', 'Potter','Sarandon', 'Jackson', 'Hendrix']
lista_de_empresas = ['Audi', 'VolksWagen', 'Ford', 'BMW', 'FIAT', 'GMC', 'Apple','Fender']
lista_de_nomes = []


def insere_telefone():
    """# 1) Inserir um campo, telefone"""
    for k, v in pessoas.items():
        # print(k, v)
        v['telefone'] = '(48)99997777'


def insere_sobrenome():
    """# 2) Sobrenomes"""
    count = 0
    for k, v in pessoas.items():
        #print(k, v)
        v['sobrenome'] = lista_de_sobrenomes[count]
        count += 1


def get_nomes():
    """Funcao que recupera nomes do dicionario pessoas"""
    for k, v in pessoas.items():
        lista_de_nomes.append(v['nome'])


def gera_email():
    """3) Funcao recebe nome, sobrenome e nome da empreasa para gerar email padronizado"""
    get_nomes() ## <<< chamei uma funcao dentro do escopo da outra

    for nome, s_nome, emp in zip(lista_de_nomes, lista_de_sobrenomes, lista_de_empresas):
        # print(nome, s_nome, emp)
        email = nome.lower() + '.' + s_nome.lower() + '@'+ emp.lower() +'.com'
        #print(email)
        lista_de_emails.append(email)


def insere_email():
    """Insere o campo email no dicionario"""
    gera_email()  ## <<< chamei uma funcao dentro do escopo da outra

    count = 0
    for k, v in pessoas.items():
        # print(k, v)
        v['email'] = lista_de_emails[count]
        count += 1


def deleta_campo():
    for k, v in pessoas.items():
        del v['sex']


def atualiza_conteudo():
    for k, v in pessoas.items():
        print(k, v)


def main():
    insere_telefone()
    #insere_sobrenome()
    insere_email()
    #deleta_campo()
    atualiza_conteudo()

main()