import random


x = int(random.randint(1, 100))
i = int(input('请猜数字：'))
if i == x:
    print('猜对了')
else:
    if i > x:
        print('大了')
        print(f'答案是{x}')
    else:
        print('小了')
        print(f'答案是{x}')
