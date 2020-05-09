import csv


def gera_csv_file():
    """Criar um arquivo .csv a partir de um .txt"""
    with open('tecnologias.txt', 'r') as file_reader:
        with open('tecnologias_2020.csv', 'w', newline='') as csv_file:
            for lines in file_reader:
                print(lines)
                writer = csv.writer(csv_file, delimiter=' ')
                writer.witerow(lines.strip().split())




# with open('tecnologias.txt', 'r') as file_reader:
#     with open('tecnologias_2020.csv', 'w', newline='') as csv_file:
#         for line in file_reader:
#             l = line.strip()
#             writer = csv.writer(csv_file, delimiter=' ')
#             writer.writerow(l.split())