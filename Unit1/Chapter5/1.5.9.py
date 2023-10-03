num = int(input('请输入数字：'))
i = num - 1
while num % i != 0:
    i -= 1
if i == 1:
    print('输入的是素数')
else:
    print('输入的不是素数')
