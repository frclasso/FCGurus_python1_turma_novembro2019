from bs4 import BeautifulSoup

# with open('simple.html', 'r') as file_reader:
#     for line in file_reader.readlines():
#         print(line, end='')


# with open('simple.html', 'r') as file_reader:
#         soup = BeautifulSoup(file_reader, 'html.parser')
#     print(soup.prettify())


# Tag
# with open('simple.html', 'r') as file_reader:
#     contents = file_reader.read()
#     soup = BeautifulSoup(contents, 'lxml')
#     print(soup.head)
#     print()
#     print(soup.title)
#     print()
#     print(soup.body)
#     print()
#     print(soup.h2)
#     print()
#     print(soup.p)

print()
# with open('simple.html', 'r') as file_reader:
#     contents = file_reader.read()
#     soup = BeautifulSoup(contents, 'lxml')
#     for child in soup.recursiveChildGenerator():
#         if child.name:
#             print(child.name)


print()
# with open('simple.html', 'r') as file_reader:
#     contents = file_reader.read()
#     soup = BeautifulSoup(contents, 'lxml')
#     new_tag = soup.new_tag('li')   # inserir uma lista
#     new_tag.string = 'Open BSD'
#
#


    # <ul>
    #     <li>OpenBSD</li>
    # </ul>

with open('simple.html', 'r') as file_reader:
    with open('simple_autalizado.html', 'a') as file_writer:
        contents = file_reader.read()
        soup = BeautifulSoup(contents, 'lxml')
        texto = 'Linux is a Amazing Operate System'
        tag = soup.p
        tag.string = texto

        content = soup.prettify()
        print(content)
        file_writer.write(content)