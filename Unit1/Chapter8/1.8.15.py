def biggest(d1):
    l1 = list()
    l2 = list(d1.values())
    l2.sort()
    for i in d1.items():
        if i[1] == l2[-1]:
            l1.append(i[0])
    print(l1)


biggest({'Theodore': 22, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20})