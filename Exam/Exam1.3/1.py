def print_narcissistic_number() -> None:
    for i in range(100, 1000):
        i1 = int(str(i)[0]) ** 3
        i2 = int(str(i)[1]) ** 3
        i3 = int(str(i)[2]) ** 3
        if i == i1 + i2 + i3:
            print(i)


print_narcissistic_number()
