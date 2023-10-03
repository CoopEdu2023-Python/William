while True:
    age = int(input('你多大了？'))
    if age < 3:
        print('门票是免费的')
    elif age <= 12:
        print('门票是十美元')
    else:
        print('门票是十五美元')
