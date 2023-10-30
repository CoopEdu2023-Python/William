def sum1(n):
    if n-2 == 0:
        return 2
    else:
        return n + sum1(n-2)


print(sum1(10))
