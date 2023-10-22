def sum_(dict1):
    x = 0
    for i in dict1.items():
        x += i[0]
        x += i[1]
    return x


print(sum_({1: 3, 4: 7, 6: 8}))
