
# controle de fluxo
# break
all_companies = ['Toyota', 'Audi', 'VW', 'BMW', 'Jeep','Tesla']
for company in all_companies:
    if company == 'BMW':
        break
    print(company)
print()

# continue
new_brands = []
for company in all_companies:
    if company == 'BMW':
        continue
    print(company)
    new_brands.append(company)
print(new_brands)

print()
print()
print()

#pass
for company in all_companies:
    if company == 'BMW':
        pass
        print('Bloco do pass')
    print('Fora do bloco pass: ', company)

