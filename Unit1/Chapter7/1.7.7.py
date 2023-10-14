def d(tuple1):
    a = set(tuple1)
    list1 = list(a)
    list1.sort()
    return tuple(list1)


print(d((1, 3, 4, 3, 7, 3, 9, 8, 6, 3)))

