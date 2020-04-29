import sys

print(f'Maior numero inteiro q seu sistema consegue gerar: {sys.maxsize}')

print('Instalcoes do Python')
for p in sys.path:
    print(p)
#
# print(sys.platform)
# print(sys.version)
# print(sys.int_info)

def get_info():
    if sys.platform.startswith('freebsd'):
        print("Welcome FreeBSD OS")
    elif sys.platform.startswith('linux'):
        print("Welcome LINUX OS")
    elif sys.platform.startswith('win32'):
        print("Welcome Microsoft Windows OS")
    elif sys.platform.startswith('darwin'):
        print("Welcome MacOSX ")
        print(f'Name: {sys.platform}')
        print(f'Versao do Python: {sys.version}')

get_info()