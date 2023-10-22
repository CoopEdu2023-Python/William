student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}


def delete(s_list):
    list1 = list()
    list2 = list()
    for i in s_list.keys():
        list1.append(i.replace(' ', ''))
        list2.append(s_list[i])
    s_list.clear()
    for i in range(len(list2)):
        s_list[list1[i]] = list2[i]
    print(s_list)


delete(student_list)
