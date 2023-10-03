import random


x = random.randint(1, 100)
win = 1
c = 0
while win:
    c += 1
    i = int(input('请猜数字：'))
    if i == x:
        print('成功了')
        win = 0
    elif i > x:
        print('大了')
    else:
        print('小了')
    if c == 5:
        print('机会已经用完')
        win = 0
