from random import randint
def make_list(start, stop, length):
    a = []
    for i in range(length):
        a.append(randint(start, stop))
    a.sort()
    print(a)

make_list(1, 20, 10)


