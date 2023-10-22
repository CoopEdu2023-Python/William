def split(dict2):
    list1 = list()
    dict1 = dict()
    for i in range(len(dict2['Science'])):
        dict1['Science'] = dict2['Science'][i]
        dict1['Language'] = dict2['Language'][i]
        list1.append(str(dict1))
    print(list1)


split({'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]})