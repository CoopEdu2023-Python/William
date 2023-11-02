num1 = "11"
num2 = "123"
list_num1 = list(num1)
list_num2 = list(num2)
num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
output1 = 0
for i in num1:
    output1 = output1 * 10 + num_dict[i]
output2 = 0
for i in num2:
    output2 = output2 * 10 + num_dict[i]
print(str(output1+output2))
