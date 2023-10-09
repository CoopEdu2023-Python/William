import math


def h(n):
    x = ''
    for i in range(n//2):
        x += ' '*((n//2)-i-1+(n % 2))
        for j in range(i*2+2-(n % 2)):
            x += '*'
        x += '\n'
    for i in range(math.ceil(n/2)):
        x += i*' '
        for j in range(n-(i*2)):
            x += '*'
        x += '\n'
    return x


print(h(5))
