def su(x):
    if x == 1:
        return False
    for c in range(2, int(x ** 0.5) + 1):
        if x % c == 0:
            return False
    return True


num = int(input('请输入一个整数：'))
print(f'{num}=', end='')
for i in range(num):
    for j in range(num):
        if not(su(j+2)):
            continue
        if num % (j + 2) == 0:
            num /= (j + 2)
            print(j+2, end='')
            if num != 1:
                print('*', end='')
            break



