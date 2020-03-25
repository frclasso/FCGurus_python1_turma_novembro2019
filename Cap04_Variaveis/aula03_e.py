
# k: v
# # name, industry, sector, headquarters, founded, notes
adidas = {
    'name':'Adidas',
    'industry':'Consumer goods',
    'sector':'Footwear',
    'headquaertes':'Herzogenaurach',
    'founded':1924,
    'notes':'Shoes, apparel and accessories',

}

print(type(adidas))
print(adidas)
print(adidas.keys())
print(adidas.values())
print(adidas.items())

print()
print()
print()

for k in adidas.values():
    print(k)

print()
print()
print()

for k,v in adidas.items():
    print(k,':',  v)