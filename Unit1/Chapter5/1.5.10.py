def su(x):
    if x == 1:
        return False
    for c in range(2, int(x ** 0.5) + 1):
        if x % c == 0:
            return False
    return True


num = int(input('请输入一个整数：'))
i = 2
print(f'{num}=', end='')
while num != 1:
    if not(su(i)):
        i += 1
        continue
    if num % i == 0:
        num /= i
        print(i, end='')
        if num != 1:
            print('*', end='')
    i += 1

