num = int(input('请输入数字：'))
s = 1
for i in range(num - 2):
    i += 2
    if num % i == 0:
        s = 0
if s:
    print('输入的是素数')
else:
    print('输入的不是素数')
