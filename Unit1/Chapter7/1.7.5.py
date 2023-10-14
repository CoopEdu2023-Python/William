m = 1
n = []
for i in range(6):
    n.append([])
    for j in range(6):
        n[i].append(m)
        m += 1

for i in range(6):
    r = 0
    c = 0
    for j in range(6):
        r += n[i][j]
        c += n[j][i]
    print(f'row{i+1}:{r}')
    print(f'column{i+1}:{c}')