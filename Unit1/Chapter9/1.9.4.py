s = 'aA12 ?'
digit = 0
alpha = 0
space = 0
other = 0
for i in s:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print(digit, alpha, space, other)