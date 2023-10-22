def present(set1, value):
    if value in set1:
        return 1
    else:
        return 0


print(present({1, 2, 4, 5, 3}, 5))
