def a(l1):
    for i in range(len(l1)):
        if type(l1[i]) == int:
            l1[i] *= 10
        elif type(l1[i]) == float:
            l1[i] = float(str(l1[i]) + '0')
        elif type(l1[i]) == str:
            l1[i] += '0'
    return l1


print(a([1, 2.0, 3, 4.0, True, 'False']))
