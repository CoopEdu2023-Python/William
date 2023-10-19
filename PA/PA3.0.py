import random


def p(piece, de, w):    # 输出棋盘的函数（棋盘的列表，标红，是否胜利）
    for j in range(9):
        # 将即将消失的棋子标红
        if de == j and w:
            print(f'\033[31;1m {piece[j]} \033[0m', end='')
        else:
            print(f' {piece[j]} ', end='')
        if j != 2 and j != 5 and j != 8:
            print('|', end='')
        else:
            print()
            if j == 2 or j == 5:
                print('———|———|———')


def win(piece):    # 判断胜利的函数
    if piece[0] == piece[1] == piece[2] == 'X' or piece[3] == piece[4] == piece[5] == 'X' or \
            piece[6] == piece[7] == piece[8] == 'X' or piece[0] == piece[3] == piece[6] == 'X' or \
            piece[1] == piece[4] == piece[7] == 'X' or piece[2] == piece[5] == piece[8] == 'X' or \
            piece[0] == piece[4] == piece[8] == 'X' or piece[2] == piece[4] == piece[6] == 'X':
        p(piece, -1, 0)
        print('=' * 30 + '获胜者：玩家1' + '=' * 30)
        return 1
    elif piece[0] == piece[1] == piece[2] == 'O' or piece[3] == piece[4] == piece[5] == 'O' or \
            piece[6] == piece[7] == piece[8] == 'O' or piece[0] == piece[3] == piece[6] == 'O' or \
            piece[1] == piece[4] == piece[7] == 'O' or piece[2] == piece[5] == piece[8] == 'O' or \
            piece[0] == piece[4] == piece[8] == 'O' or piece[2] == piece[4] == piece[6] == 'O':
        p(piece, -1, 0)
        print('=' * 30 + '获胜者：玩家2' + '=' * 30)
        return 2
    return 0


# 主函数
# 阅读后的开始按钮
con = ''
# 棋盘的数字与名字
chessboard = ['r', 't', 'y', 'f', 'g', 'h', 'v', 'b', 'n']
# 开始部分的提示
print('不同位置的输入（和键盘的形状是一样的哦）')
print(' r | t | y ' + '\n' + '———|———|———' + '\n' + ' f | g | h ' + '\n' + '———|———|———' + '\n' + ' v | b | n ')
while con != 'x' and con != 'X':
    con = input("玩家阅读后请输入”X“或“x”表示已经准备：")
# 随机哪位玩家先手，x=1是玩家1，x=2是玩家2
x = random.randint(1, 2)
# who变量是了解玩家顺序的变量
if x == 0:
    who = 'X'
else:
    who = 'O'

# 输入并调用函数显示每一步的变化
while 1:
    # 记录下棋的数字位置
    record_num = []
    # 每个位置的状态
    list_piece = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # 循环次数的计数
    game_num = 1
    # 初始化要删除的内容
    delete = -1
    print('\n' * 50 + f"玩家{x % 2 + 1}号的回合：")
    while not win(list_piece):
        # 即将删除的内容的位置
        if game_num > 6:
            delete = record_num[game_num - 7]
        # 输出棋盘
        p(list_piece, delete, 1)
        if game_num > 6:
            print(f'{chessboard[record_num[game_num - 7]]}位置的棋子即将消失')
        # flag是为了让continue可以作用到while循环，这里是为了初始化flag
        flag = 'p'
        # 输入
        where = input('请输入落子位置:')
        # 遍历
        for i in range(9):
            # 使键盘的输入与棋盘上的变化一一对应
            if where == chessboard[i]:
                # 防止下到已经下过的地方
                if list_piece[i] != ' ':
                    print('\n' * 50 + '这里已经下过了，请换一个位置' + '\n' + f"玩家{x}号的回合：")
                    # continue的标志,跳出循环运行continue
                    flag = 'c'
                    break
                list_piece[i] = who
                record_num.append(i)
                break
            # 防止下到不在棋盘上的的地方
            if i == 8:
                print('\n' * 50 + '棋盘上没有这个位置，请换一个位置' + '\n' + f"玩家{x}号的回合：")
                # continue的标志,跳出循环运行continue
                flag = 'c'
                break
        # 当输入错误时运行此代码
        if flag == 'c':
            continue
        # 保证棋盘上最多六个棋子
        if game_num > 6:
            list_piece[record_num[game_num - 7]] = ' '
            print()
        # 回合转换
        if who == 'X':
            print('\n' * 50 + "玩家2号的回合：")
            who = 'O'
        else:
            print('\n' * 50 + "玩家1号的回合：")
            who = 'X'
        # 记录局数
        game_num += 1
    # 更新局数
    x += 1
    # 推出或继续游戏
    con = input('推出游戏请输出X，否则随意输出其他字母')
    if con == 'X' or con == 'x':
        break
