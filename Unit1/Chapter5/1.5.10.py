num = int(input('请输入一个整数：'))
i = 1
print(f'{num}=', end='')
while num != 1:
    if num % i == 0:
        num /= i
        print(i, end='')
        if num != 1:
            print('*', end='')
    i += 1
