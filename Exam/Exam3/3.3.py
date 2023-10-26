def find_sum_of_3(num_list: list) -> list[tuple]:
    r = []
    for i in range(len(num_list)):
        for j in range(1, len(num_list)):
            for z in range(2, len(num_list)):
                x = (num_list[i], num_list[j], num_list[z])
                if i != j and i != z and j != z and num_list[i] + num_list[j] + num_list[z] == 0 and x not in r:
                    r.append(x)
    return r


print(find_sum_of_3([-1, 0, 1, 2, -1, -4]))
