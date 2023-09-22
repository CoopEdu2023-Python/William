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
def you_wu(zf):
    if zf != ' ':
        print('\n' * 50)
        print('输入无效')
        print("玩家1号的回合：")
        return 1


import random

print('玩家1的操控按键，棋子为 ”X“，下棋时请输入小写字母 ')
print(' q | w | e ' + '\n' + '———|———|———' + '\n' + ' a | s | d ' + '\n' + '———|———|———' + '\n' + ' z | x | c ')
继续 = input("玩家1阅读后请输入”X“或“x”表示已经准备：")
if 继续 != 'x' and 继续 != 'X':
    exit()
print('玩家2的操控按键，棋子为 “O”或“o”，下棋时请输入小写字母 ')
print(' u | i | o ' + '\n' + '———|———|———' + '\n' + ' j | k | l ' + '\n' + '———|———|———' + '\n' + ' m | , | . ')
继续 = input("玩家2阅读后请输入”O“表示已经准备：")
if 继续 != 'o' and 继续 != 'O':
    exit()
print('\n' * 50)
先手 = random.randint(1, 2)
print(f"玩家{先手}号的回合：")
r, t, y, f, g, h, v, b, n = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
次数 = 0
while p(r, t, y, f, g, h, v, b, n) == 0:
    if 次数 == 9:
        print('游戏结束，平局')
        exit()
    input_1 = ''
    input_2 = ''
    if 先手 == 1:
        input_1 = input('请输入落子位置:')
        if input_1 == 'q':
            if you_wu(r):
                continue
            r = 'X'
        elif input_1 == 'w':
            if you_wu(t):
                continue
            t = 'X'
        elif input_1 == 'e':
            if you_wu(y):
                continue
            y = 'X'
        elif input_1 == 'a':
            if you_wu(f):
                continue
            f = 'X'
        elif input_1 == 's':
            if you_wu(g):
                continue
        elif input_1 == 'd':
            if you_wu(h):
                continue
            h = 'X'
        elif input_1 == 'z':
            if you_wu(v):
                continue
            v = 'X'
        elif input_1 == 'x':
            if you_wu(b):
                continue
            b = 'X'
        elif input_1 == 'c':
            if you_wu(n):
                continue
            n = 'X'
        else:
            print('\n' * 50)
            print('输入无效')
            print("玩家1号的回合：")
            continue
    else:
        input_2 = input('请输入落子位置:')
        if input_2 == 'u':
            if you_wu(r):
                continue
            r = 'O'
        elif input_2 == 'i':
            if you_wu(t):
                continue
            t = 'O'
        elif input_2 == 'o':
            if you_wu(y):
                continue
            y = 'O'
        elif input_2 == 'j':
            if you_wu(f):
                continue
            f = 'O'
        elif input_2 == 'k':
            if you_wu(g):
                continue
            g = 'O'
        elif input_2 == 'l':
            if you_wu(h):
                continue
            h = 'O'
        elif input_2 == 'm':
            if you_wu(v):
                continue
            v = 'O'
        elif input_2 == ',':
            if you_wu(b):
                continue
            b = 'O'
        elif input_2 == '.':
            if you_wu(n):
                continue
            n = 'O'
        else:
            print('\n' * 50)
            print('输入无效')
            print("玩家2号的回合：")
            continue
    print('\n' * 50)
    if 先手 == 1:
        print("玩家2号的回合：")
        先手 = 2
    else:
        print("玩家1号的回合：")
        先手 = 1
    次数 += 1
