import random


x = random.randint(1, 100)
win = 1
while win:
    i = int(input('请猜数字：'))
    if ((i - x) ** 2) ** 0.5 == 0:
        print('成功了')
        win = 0
    elif ((i - x) ** 2) ** 0.5 <= 10:
        print('接近了')
    elif ((i - x) ** 2) ** 0.5 > 50:
        print('有点远')
    elif ((i - x) ** 2) ** 0.5 > 30:
        print('错误')

