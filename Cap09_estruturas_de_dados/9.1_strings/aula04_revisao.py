

# strings

cliente1 = ['FABIO', 'REIS' ,'Classo', '.111.222.333', '123456778', '(48)9234-5678']
# nome, sobrenome, cpf, idt, telefone, email

nome = cliente1[0]

sobrenome_1 = cliente1[1]
sobrenome_2 = cliente1[2]
cpf = cliente1[3]
idt = cliente1[4]
tel = cliente1[5]

email = nome.lower() +'.'+ sobrenome_2.lower() + '@empresa.com.br'
print(email)

# zfill
cpf_new = cpf.zfill(15)
print(cpf_new)

idt_new = idt.zfill(11)
print(idt_new)

# remover  ()  -
# adionar 9
tel_new= []
indesejaveis = ['(', ')', '-']
for t in tel:
    #print(t, end='')
    if t in indesejaveis:
        tel.split(t)
    else:
        tel_new.append(t) # append insere no final da lista

print(tel_new)
tel_new.insert(2, '9') # insert a posicao e o caracter
print(tel_new)
telefone = ''.join(tel_new)

cliente1_atualizado = [nome.upper(), sobrenome_1.upper(), sobrenome_2.upper(),cpf_new, idt_new, telefone]
print(cliente1_atualizado)
