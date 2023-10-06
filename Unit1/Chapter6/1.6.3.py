import math


def h(n):
    for i in range(n//2):
        print(' '*((n//2)-i), end='')
        for j in range(i*2+1):
            print('*', end='')
        print('')
    for i in range(math.ceil(n/2)):
        print(i*' ', end='')
        for j in range(n-(i*2)):
            print('*', end='')
        print('')


h(5)
