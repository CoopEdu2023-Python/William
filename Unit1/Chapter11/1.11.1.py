def sum1(list1):
    if len(list1) == 1:
        if type(list1[0]) == list:
            return sum1(list1[0])
        else:
            return list1[0]
    else:
        if type(list1[0]) == list:
            return sum1(list1[0]) + sum1(list1[1:])
        else:
            return list1[0] + sum1(list1[1:])


print(sum1([1, 2, [3, 4], [5, 6]]))

# list_1 = [1, 2, [3, 4], [5, 6]]
# print(len(list_1[1:2]), list_1[1:2])
# print(list_1[0])
# s = list_1[1:]
# print(s, s[0])
