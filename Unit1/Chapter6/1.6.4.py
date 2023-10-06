def c(x):
    for i in range(x):
        for j in range(i+1):
            print(f'{j+1} * {i+1} = {(i+1) * (j+1)}', end='    ')
        print('')


c(9)
