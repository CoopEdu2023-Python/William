m = int(input('m = '))
n = int(input('n = '))
num = 0
for i in range(n):
    print(str(m)*(i+1), end='')
    num += int(str(m)*(i+1))
    if i != n-1:
        print('+', end='')
print(f'={num}')
