
# ler um json

# caso 1

# with open('a_movie.json', 'r') as json_reader:
#     #print(json_reader.read())
#     for line in json_reader.readlines():
#         print(line,end='')


# caso2
import json

with open('a_movie.json', 'r') as json_reader:
    with open('copia_a_movie.json','w') as json_writer:
        data = json.load(json_reader)
        data['Country'] = 'Brasil'
        json.dump(data, json_writer, indent=1)


# leitor
with open('copia_a_movie.json', 'r') as reader:
    print(reader.read())