list1 = [1, 3, 4, 7, 9, 8, 6, 3]
list1.sort()
while len(list1) > 1:
    list1.append(list1.pop(0) * list1.pop(0) + 1)
print(list1[0])
