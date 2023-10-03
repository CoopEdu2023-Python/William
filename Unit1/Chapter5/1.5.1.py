num = 1
while num % 10 != 0:
    num = int(input('请输入数字：'))
    if num % 10 == 0:
        print('是十的倍数')
    else:
        print('不是十的倍数')
1