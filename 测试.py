class Phone2021:
    def __init__(self):
        self.OS = 'IOS'

    def new(self):
        print('lightning 接口')


class Phone2022:
    def new(self):
        print('灵动岛')


class Phone2023(Phone2022, Phone2021):  # 继承了Phone2022的属性与方法

    def __init__(self):
        super().__init__()
        self.OS = 'CNMIOS'

    def type_c(self):
        print('type-c 充电口史诗级更新')
        Phone2021().new()
        print(f'上一代的系统为{Phone2021().OS}')


a = Phone2023()
a.new()
print(a.OS)
