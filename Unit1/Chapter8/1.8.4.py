def biggest(set1):
    list1 = list(set1)
    list1.sort()
    return list1[0], list1[-1]


print(biggest({1, 2, 8, 9, 5, 6}))