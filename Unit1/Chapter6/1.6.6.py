def c(x):
    n = ''
    for i in range(x):
        for j in range(i+1):
            n += f'{j+1} * {i+1} = {(i+1) * (j+1)}    '
        n += '\n'
    return n


print(c(9))
