alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_lower = alpha_upper.casefold()
for i in input():
    if i.isupper():
        print(alpha_upper[-alpha_upper.index(i)-1], end='')
    else:
        print(alpha_lower[-alpha_lower.index(i)-1], end='')
