import Phone

p = Phone
print(p)
print(dir(p))

from Phone.g3 import cpf

print(cpf)


import sound.effects.echo as efeito

print(dir(efeito))
e = efeito.echo_effect
print(e)


from sound.effects.echo import echo_effect   # <<<
print(echo_effect)