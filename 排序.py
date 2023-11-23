def sort1(list1):
    x = len(list1)
    for i in range(x):
        for j in range(x - i - 1):
            if list1[j] <= list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    for i in range(x // 2):
        for j in range(x // 2 + x % 2, x - i - 1):
            if list1[j] >= list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(list1)


sort1([43, 5, 4, 88, 3, 33, 8, 3, 5])
sort1([3, 4, 1, 7, 2, 66])
sort1([55, 1, 4, 1, 2, 5, 8])
