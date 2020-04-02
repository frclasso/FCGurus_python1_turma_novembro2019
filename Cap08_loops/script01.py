

# for n in '1200':
# #     print(n)

jeep_info = 'Jeep é uma marca Americana de automoveis pertencente ao grupo FCA...'

all_companies = ['Toyota', 'Audi', 'VW', 'BMW', 'Jeep','Tesla']
for company in all_companies:
    if company == 'Jeep':
        print(jeep_info)

#print(len(all_companies))

count = 0
while count < len(all_companies):
    # print(all_companies[count])
    if all_companies[count] == 'Jeep':
        print(jeep_info)
    count += 1