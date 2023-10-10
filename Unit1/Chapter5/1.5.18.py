import math


n = int(input('请输入行数：'))
for i in range(n//2):
    print(' '*((n//2)-i-1+(n % 2)), end='')
    print('*'*(i*2+2-(n % 2)), end='')
    print('')
for i in range(math.ceil(n/2)):
    print(i*' ', end='')
    print('*'*(n-(i*2)), end='')
    print('')
