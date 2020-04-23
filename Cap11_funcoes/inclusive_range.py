
print(range(25))
print(range(0, 25, 5))
print(list(range(0, 25)))
# 0 ... 25
# start/inicio
# stop/fim
# step


def inclusive_range(start, stop, step):
    """Inlcuir o valor final do range"""
    i = start
    while i <= stop:
        yield i
        i += step


def main():
    for i in inclusive_range(0, 25, 1):
        print(i, end=' ')

main()