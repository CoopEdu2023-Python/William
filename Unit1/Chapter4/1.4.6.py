age = int(input('你多大了：'))
if age >= 65:
    print('你是个老年人')
elif age >= 18:
    print('你是个成年人')
    if age <= 20:
        print('你是个青少年')
    if age <= 24:
        print('你是个年轻人')
elif 15 <= age <= 24:

    print('你是个年轻人')
    if age <= 20:
        print('你是个青少年')
elif 13 <= age <= 20:
    print('你是个青年人')
elif age <= 3:
    print('你是个孩子')
elif age <= 2:
    print('你是一个蹒跚学步的孩子')
else:
    print('你是个婴儿')
