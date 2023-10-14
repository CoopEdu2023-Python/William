def d(list1, di):
    list1.sort()
    del list1[0: 2]
    del list1[3: 5]
    s = 0
    for i in range(3):
        s += list1[i]
    s /= 3
    s *= di
    return s


list_1 = [7, 8, 6, 5, 9, 7, 10]
print(d(list_1, 8))
