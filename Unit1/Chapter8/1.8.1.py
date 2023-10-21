def difference(a, b):
    c = a | b
    a = a & b
    c = c - a
    return c


print(difference({1, 2, 3}, {3, 4}))
