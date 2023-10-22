def mix(l1, l2):
    dict1 = dict()
    if len(l1) >= len(l2):
        for i in range(len(l2)):
            dict1[l1[i]] = l2[i]
    else:
        for i in range(len(l1)):
            dict1[l1[i]] = l2[i]
    print(dict1)


mix(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5])