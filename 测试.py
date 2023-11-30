a = 'AEIOUaeiou'
x = list()
s = list(s)
for i in s:
    if i in a:
        x.append(i)

num = 0
n = 0
r = list()
for i in s:
    if i in a:
        num += 1
        r.insert(n, x[0 - num])
    else:
        r.append(i)
    n += 1
r = ''.join(r)
return r
