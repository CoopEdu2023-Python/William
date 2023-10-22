def delete(dict1):
    part = list(dict1.values())
    j = list()
    for i in dict1.items():
        part.remove(i[1])
        if i[1] in part:
            j.append(i[0])
        part.append((i[1]))
    for i in j:
        dict1.pop(i)
    print(dict1)


sample_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
   'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
   'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}
delete(sample_data)