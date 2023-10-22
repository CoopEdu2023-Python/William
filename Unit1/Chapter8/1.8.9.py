def add(dict1, dict2):
    for i in dict2.items():
        dict1[i[0]] = i[1]
    return dict1


print(add({1: 2, 3: 5}, {1: 8, 4: 5}))
