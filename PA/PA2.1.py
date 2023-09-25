import random


# 输出和判断胜利
def p(r, t, y, f, g, h, v, b, n):
    print(f' {r} | {t} | {y} '+'\n'+'———|———|———'+'\n'+f' {f} | {g} | {h} '+'\n'+'———|———|———'+'\n'+f' {v} | {b} | {n}')
    if r == t == y == 'X' or f == g == h == 'X' or v == b == n == 'X' or r == f == v == 'X' or\
            t == g == b == 'X' or y == h == n == 'X' or r == g == n == 'X' or y == g == v == 'X':
        print('获胜者：玩家1')
        return 1
    elif r == t == y == 'O' or f == g == h == 'O' or v == b == n == 'O' or r == f == v == 'O' or\
            t == g == b == 'O' or y == h == n == 'O' or r == g == n == 'O' or y == g == v == 'O':
        print('获胜者：玩家2')
        return 2
    return 0


# 主函数
# 开始部分的提示
print('不同位置的输入（和键盘的形状是一样的哦）')
print(' r | t | y ' + '\n' + '———|———|———' + '\n' + ' f | g | h ' + '\n' + '———|———|———' + '\n' + ' v | b | n ')
# 阅读后的开始按钮
con = ''
while con != 'x' and con != 'X':
    con = input("玩家阅读后请输入”X“或“x”表示已经准备：")
# 随机哪位玩家先手，x=1是玩家1，x=2是玩家2
x = random.randint(1, 2)
# who变量是了解玩家顺序的变量
if x == 1:
    who = 'X'
else:
    who = 'O'
print('\n' * 50 + f"玩家{x}号的回合：")
# 循环次数的计数
num = 1
# 创建字典dict_1记录每一个位置的状态
# 创建一个字典dict_2记录每一步旗子的记录，方便控制棋子数量
dict_1 = {'r': ' ', 't': ' ', 'y': ' ', 'f': ' ', 'g': ' ', 'h': ' ', 'v': ' ', 'b': ' ', 'n': ' '}
list_1 = []
# 输入并调用函数显示每一步的变化
while p(dict_1['r'], dict_1['t'], dict_1['y'], dict_1['f'], dict_1['g'], dict_1['h'], dict_1['v'],
        dict_1['b'], dict_1['n']) == 0:
    # flag是为了让continue可以作用到while循环，这里是为了初始化flag
    flag = 'p'
    # 输入
    it = input('请输入落子位置:')
    # 遍历
    for i in 'rtyfghvbn':
        # 使键盘的输入与棋盘上的变化一一对应
        if it == i:
            # 防止下到已经下过的地方
            if dict_1[i] != ' ':
                print('\n' * 50 + '这里已经下过了，请换一个位置' + '\n' + f"玩家{x}号的回合：")
                # continue的标志,跳出循环运行continue
                flag = 'c'
                break
            dict_1[i] = who
            list_1.insert(num-1, i)
            break
        # 防止下到不在棋盘上的的地方
        if i == 'n':
            print('\n' * 50 + '棋盘上没有这个位置，请换一个位置' + '\n' + f"玩家{x}号的回合：")
            # continue的标志,跳出循环运行continue
            flag = 'c'
            break
    # 当输入错误时运行此代码
    if flag == 'c':
        continue
    # 保证棋盘上最多六个棋子
    if num > 6:
        dict_1[list_1[num-7]] = ' '
    # 回合转换
    if who == 'X':
        print('\n' * 50 + "玩家2号的回合：")
        who, x = 'O', 2
    else:
        print('\n' * 50 + "玩家1号的回合：")
        who, x = 'X', 1
    # 记录局数
    num += 1
