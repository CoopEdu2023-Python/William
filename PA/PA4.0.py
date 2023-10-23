import random
import time


# 输出棋盘的函数（棋盘的列表，标红，是否胜利）
def chessboard_print(piece, delete_piece, whether_print_red):
    for j in range(9):
        # 将即将消失的棋子标红
        if delete_piece == j and whether_print_red:
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
    print('=' * 10 + string + '=' * 10, end='')
    if end:
        print()


# 玩法选择
def playing_method():
    print('\n'*50)
    choose = ' '
    while choose != '1' and choose != '2':
        print("请选择游戏模式：", "1.普通模式", "2.进阶模式", '(输入1或2）', sep='\n', end='')
        choose = input()
    return int(choose) - 1


# 判断胜利的函数
def win(piece):

    if piece[0] == piece[1] == piece[2] == 'X' or piece[3] == piece[4] == piece[5] == 'X' or \
            piece[6] == piece[7] == piece[8] == 'X' or piece[0] == piece[3] == piece[6] == 'X' or \
            piece[1] == piece[4] == piece[7] == 'X' or piece[2] == piece[5] == piece[8] == 'X' or \
            piece[0] == piece[4] == piece[8] == 'X' or piece[2] == piece[4] == piece[6] == 'X':

        chessboard_print(piece, -1, 0)
        important_print('获胜者：玩家X', 1)
        return 1

    elif piece[0] == piece[1] == piece[2] == 'O' or piece[3] == piece[4] == piece[5] == 'O' or \
            piece[6] == piece[7] == piece[8] == 'O' or piece[0] == piece[3] == piece[6] == 'O' or \
            piece[1] == piece[4] == piece[7] == 'O' or piece[2] == piece[5] == piece[8] == 'O' or \
            piece[0] == piece[4] == piece[8] == 'O' or piece[2] == piece[4] == piece[6] == 'O':

        chessboard_print(piece, -1, 0)
        important_print('获胜者：玩家O', 1)
        return 2

    return 0


# 主函数
game_continues = ' '
chessboard = ['r', 't', 'y', 'f', 'g', 'h', 'v', 'b', 'n']

# 开始部分的提示
print(' ' * 6 + '不同位置的输入（和键盘的形状是一样的哦）')
print(' ' * 16 + ' r | t | y ' + '\n' +
      ' ' * 16 + '———|———|———' + '\n' +
      ' ' * 16 + ' f | g | h ' + '\n' +
      ' ' * 16 + '———|———|———' + '\n' +
      ' ' * 16 + ' v | b | n ')
while game_continues != '':
    important_print("玩家阅读后,请输入回车继续游戏", 0)
    game_continues = input()

while 1:
    game_mode = playing_method()

    if random.randint(1, 2) == 2:  # 随机先手
        who = 'X'
    else:
        who = 'O'

    record_num = []  # 记录下棋的数字位置
    list_piece = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 每个位置的状态
    game_num = 1  # 循环次数的计数
    delete = -1  # 初始化要删除的内容
    print('\n' * 50 + f"玩家{who}的回合：")
    while not win(list_piece):
        flag = '初始化flag'
        if game_num > 6:  # 即将删除的内容的位置
            delete = record_num[game_num - 7]
        chessboard_print(list_piece, delete, game_mode)  # 输出棋盘
        if game_num > 6 and game_mode:
            print(f'{chessboard[record_num[game_num - 7]]}位置的棋子即将消失')

        where = input('请输入落子位置:')
        for i in range(9):
            if where == chessboard[i]:
                # 防止下到已经下过的地方
                if game_num > 6:
                    if record_num[game_num - 7] == i:
                        flag = '落子位置即将删除'
                elif list_piece[i] != ' ':
                    print('\n' * 50 + '这里已经下过了，请换一个位置' + '\n' + f"玩家{who}的回合：")
                    flag = '输入错误'
                    break

                list_piece[i] = who
                record_num.append(i)
                break

            # 防止下到不在棋盘上的的地方
            if i == 8:
                print('\n' * 50 + '棋盘上没有这个位置，请换一个位置' + '\n' + f"玩家{who}的回合：")
                flag = '输入错误'
                break
        if flag == '输入错误':
            continue

        # 保证棋盘上最多六个棋子
        if game_num > 6 and flag != '落子位置即将删除' and game_mode:
            list_piece[record_num[game_num - 7]] = ' '
            print()

        # 回合转换
        if who == 'X':
            print('\n' * 50 + "玩家O的回合：")
            who = 'O'
        else:
            print('\n' * 50 + "玩家X的回合：")
            who = 'X'

        game_num += 1  # 记录局数

    time.sleep(2)
    print('\n' * 50)
    important_print('退出游戏请输X，继续游戏请回车', 0)
    game_continues = input()
    if game_continues == 'X' or game_continues == 'x':
        break
