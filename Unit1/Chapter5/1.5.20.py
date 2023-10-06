while 1:
    num = int(input('请输入数字：'))
    for i in range(num):
        if num % (i+1) == 0:
            print(i+1)
