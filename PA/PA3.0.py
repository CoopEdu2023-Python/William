import random
import time


# 输出棋盘的函数（棋盘的列表，标红，是否胜利）
def chessboard_print(piece, de, w):
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


# 输出重点文字
def important_print(string, end):
    if end:
        print('=' * 10 + string + '=' * 10)
    else:
        print('=' * 10 + string + '=' * 10, end='')


# 判断胜利的函数
def win(piece):

    if piece[0] == piece[1] == piece[2] == 'X' or piece[3] == piece[4] == piece[5] == 'X' or \
            piece[6] == piece[7] == piece[8] == 'X' or piece[0] == piece[3] == piece[6] == 'X' or \
            piece[1] == piece[4] == piece[7] == 'X' or piece[2] == piece[5] == piece[8] == 'X' or \
            piece[0] == piece[4] == piece[8] == 'X' or piece[2] == piece[4] == piece[6] == 'X':

        chessboard_print(piece, -1, 0)
        important_print('获胜者：玩家1', 1)
        return 1

    elif piece[0] == piece[1] == piece[2] == 'O' or piece[3] == piece[4] == piece[5] == 'O' or \
            piece[6] == piece[7] == piece[8] == 'O' or piece[0] == piece[3] == piece[6] == 'O' or \
            piece[1] == piece[4] == piece[7] == 'O' or piece[2] == piece[5] == piece[8] == 'O' or \
            piece[0] == piece[4] == piece[8] == 'O' or piece[2] == piece[4] == piece[6] == 'O':

        chessboard_print(piece, -1, 0)
        important_print('获胜者：玩家2', 1)
        return 2

    return 0


# 主函数
# 阅读后的开始按钮
proceed = ' '
# 棋盘的数字与名字
chessboard = ['r', 't', 'y', 'f', 'g', 'h', 'v', 'b', 'n']
# 开始部分的提示
print(' ' * 6 + '不同位置的输入（和键盘的形状是一样的哦）')
print(' ' * 16 + ' r | t | y ' + '\n' +
      ' ' * 16 + '———|———|———' + '\n' +
      ' ' * 16 + ' f | g | h ' + '\n' +
      ' ' * 16 + '———|———|———' + '\n' +
      ' ' * 16 + ' v | b | n ')
while proceed != '':
    important_print("玩家阅读后,请输入回车继续游戏", 0)
    proceed = input()
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
        chessboard_print(list_piece, delete, 1)
        if game_num > 6:
            print(f'{chessboard[record_num[game_num - 7]]}位置的棋子即将消失')
        # flag是为了让continue可以作用到while循环，这里是为了初始化flag
        flag = '初始化输入'
        # 输入
        where = input('请输入落子位置:')
        # 遍历
        for i in range(9):
            # 使键盘的输入与棋盘上的变化一一对应
            if where == chessboard[i]:
                # 防止下到已经下过的地方
                if game_num > 6:

                    if record_num[game_num - 7] == i:
                        flag = '落子位置即将删除'
                elif list_piece[i] != ' ':
                    print('\n' * 50 + '这里已经下过了，请换一个位置' + '\n' + f"玩家{x}号的回合：")
                    # continue的标志,跳出循环运行continue
                    flag = '输入错误'
                    break
                list_piece[i] = who
                record_num.append(i)
                break
            # 防止下到不在棋盘上的的地方
            if i == 8:
                print('\n' * 50 + '棋盘上没有这个位置，请换一个位置' + '\n' + f"玩家{x}号的回合：")
                # continue的标志,跳出循环运行continue
                flag = '输入错误'
                break
        # 当输入错误时运行此代码
        if flag == '输入错误':
            continue
        # 保证棋盘上最多六个棋子
        if game_num > 6 and flag != '落子位置即将删除':
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
    time.sleep(2)
    print('\n' * 50)
    important_print('退出游戏请输X，继续游戏请回车', 0)
    con = input()
    if con == 'X' or con == 'x':
        break
