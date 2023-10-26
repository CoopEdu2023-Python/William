def max_product(num_list: list) -> int:
    r = []
    for i in range(len(num_list)):
        for j in range(1, len(num_list)):
            for z in range(2, len(num_list)):
                if i != j and i != z and j != z:
                    r.append(num_list[i] * num_list[j] * num_list[z])
    return max(r)


print(max_product([1, 2, -3, -3, 0]))
