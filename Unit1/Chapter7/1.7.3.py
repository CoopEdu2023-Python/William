def d(list1):
    for i in range(len(list1)):
        if type(list1[i]) == int or type(list1[i]) == float:
            list1[i] *= 2
    return list1


print(d([1, 2.0, 3, 4.0, True, 'False']))