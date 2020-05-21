import pandas as pd
import numpy as np

data = pd.read_excel('feira.xlsx')
# print(data.info)
# print(data.head())  # sem parametro 5 primeiras linhas
# print(data.tail())  # sem parametro 5 ultimas linhas


df = pd.DataFrame(data, columns=[
    'PRODUCE',
    'COST PER POUND',
    'POUNDS SOLD',
    'TOTAL'
])

#print(df.head())
produtos = df['PRODUCE']
# print(produtos.head())
custo_por_libra = df['COST PER POUND']
qtd = df['POUNDS SOLD']
total = custo_por_libra * qtd
df['TOTAL'] = total

df['TOTAL'] = df['TOTAL'].round(2)
print(df.head(30))
print()
print()

# Filtro
# Soma dos totais
print(max(df['TOTAL']))
print(min(df['TOTAL']))
print(df['TOTAL'].sum().round(2))
# print(max(df.loc[df['TOTAL'].idxmax()]))


# df.to_csv('frutas2.csv')

# import csv
# with open('frutas.csv', 'w') as csv_writer:
#     writer = csv.writer(csv_writer)
#     writer.writerow(df.columns)
#     for lines in df.values:
#         writer.writerow(lines)