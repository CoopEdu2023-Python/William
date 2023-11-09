def print_perfect_number() -> None:
    for i in range(1, 1000):
        r = []
        for j in range(1, i):
            if i % j == 0:
                r.append(j)
        if sum(r) == i:
            print(i)


print_perfect_number()
