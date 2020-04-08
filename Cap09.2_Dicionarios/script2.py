

pessoas = {
    1:{'nome':'John', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    2:{'nome':'Jane', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    3:{'nome':'Mary', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    4:{'nome':'Peter', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    5:{'nome':'Harry', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    6:{'nome':'Susan', 'sobrenome':'Doe', 'idade':20, 'sex':'F'},
    7:{'nome':'Andrey', 'sobrenome':'Doe', 'idade':20, 'sex':'M'},
    8:{'nome':'Jimmy', 'sobrenome':'', 'idade':20, 'sex':'M'},
}

for k, v in pessoas.items():
    #print(k, v)
    for chave, valor in v.items():
        pass
        #print(v)
    v['tel'] = 'None'
    print(v)

### ATIVIDADE

# email

# sobrenome
# passar valores padrao (setdefault(), fromkeys(), get())

#remover colunar 'sex'


