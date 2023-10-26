def add(str1, list1):
    string = ''
    for i in list1:
        string += i
        string += str1
    return string


print(add('123', ['a', 'b', 'c']))