def set_1(set1, set2):
    for i in set2:
        if not(i in set1):
            return 0
    else:
        return 1


print(set_1({1, 2, 3}, {1, 3}))