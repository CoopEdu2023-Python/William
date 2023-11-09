while 1:
    a = float(input('请输入第一个数字：'))
    b = float(input('请输入第二个数字：'))
    c = input('请选择你所使用的符号：')
    if c == '/':
        if b == 0:
            print('零不能作为除数')
            continue
        else:
            print(f"{a}{c}{b}={a/b}")
    elif c == "+":
        print(f"{a}{c}{b}={a+b}")
    elif c == '-':
        print(f"{a}{c}{b}={a-b}")
    elif c == '*':
        print(f"{a}{c}{b}={a*b}")
    else:
        print('输入错误，请重新输入')
