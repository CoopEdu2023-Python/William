def p(r, t, y, f, g, h, v, b, n):
    print(f' {r} | {t} | {y} '+'\n'+'———|———|———'+'\n'+f' {f} | {g} | {h} '+'\n'+'———|———|———'+'\n'+f' {v} | {b} | {n} ')
    if r == t == y == 'X' or f == g == h == 'X' or v == b == n == 'X' or r == f == v == 'X' or\
            t == g == b == 'X' or y == h == n == 'X' or r == g == n == 'X' or y == g == v == 'X':
        print('获胜者：玩家1')
        return 1
    elif r == t == y == 'O' or f == g == h == 'O' or v == b == n == 'O' or r == f == v == 'O' or\
            t == g == b == 'O' or y == h == n == 'O' or r == g == n == 'O' or y == g == v == 'O':
        print('获胜者：玩家2')
        return 2
    return 0
def f1():
    print('\n' * 50)
    print('输入无效')
    print(f"玩家{x}号的回合：")
import random
print('不同位置的输入（和键盘的形状是一样的哦）')
print(' r | t | y ' + '\n' + '———|———|———' + '\n' + ' f | g | h ' + '\n' + '———|———|———' + '\n' + ' v | b | n ')
继续 = input("玩家阅读后请输入”X“或“x”表示已经准备：")
if 继续 != 'x' and 继续 != 'X':
    exit()
print('\n' * 50)
x = random.randint(1, 2)
if x == 1:
    先手 = 'X'
else:
    先手 = 'O'
print(f"玩家{x}号的回合：")
次数 = 0
dict_1 = {'r': ' ', 't': ' ', 'y': ' ', 'f': ' ', 'g': ' ', 'h': ' ', 'v': ' ', 'b': ' ', 'n': ' '}
while p(dict_1['r'], dict_1['t'], dict_1['y'], dict_1['f'], dict_1['g'], dict_1['h'], dict_1['v'], dict_1['b'], dict_1['n']) == 0:
    flag = 'p'
    if 次数 == 9:
        print('游戏结束，平局')
        exit()
    it = ''
    it = input('请输入落子位置:')
    for i in 'rtyfghvbn':
        if it == i:
            if dict_1[i] != ' ':
                f1()
                flag = 'c'
                break
            print('\n' * 50)
            dict_1[i] = 先手
            break
        if i == 'n':
            f1()
            flag = 'c'
            break
    if flag == 'c':
        continue
    if 先手 == 'X':
        print("玩家2号的回合：")
        先手 = 'O'
        x = 2
    else:
        print("玩家1号的回合：")
        先手 = 'X'
        x = 1
    次数 += 1
