def sum1(n):
    if 2 ** n == 1:
        return 1
    else:
        return 1/(2**n) + sum1(n-1)


print(sum1(7))
