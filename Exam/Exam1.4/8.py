s = "abcdefg"
k = 2
s = list(s)
for i in range(len(s) // (k*2) + 1):
    for j in range(k // 2):
        s.insert(i*k*2+k//2, s.pop(j+i*k*2))
print(s)
