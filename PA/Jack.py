from termcolor import colored

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
count_list = [0, 0, 0, 0, 0, 0]  # 记录前六次下棋位置
count_locate = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]  # 记录前六次下棋的坐标


def print_pan(board_):  # 输出棋盘
    i = 0
    while i < 3:
        print(f" %s | %s | %s " % (board_[i][0], board_[i][1], board_[i][2]))
        i += 1
        if i == 3:
            break
        print(f"---|---|---")


def check(board_):  # 检查是否有人获胜
    for i in range(3):
        if board_[i][0] == board_[i][1] == board_[i][2] and board_[i][0] != " ":
            return True
    for i in range(3):
        if board_[0][i] == board_[1][i] == board_[2][i] and board_[0][i] != " ":
            return True
    if board_[0][0] == board_[1][1] == board_[2][2] and board_[0][0] != ' ':
        return True
    if board_[0][2] == board_[1][1] == board_[2][0] and board_[0][2] != ' ':
        return True
    return False


def count(m, n):  # 记录每次下棋的位置和对应的棋子，判断是否超过第六次，如果有就消除前六次之前的步数
    if m >= 6:
        print(colored(f"hey！下一回合位置{n}上的棋子就disappear啦！！", "red"))
    if m >= 7:
        board[count_locate[m % 6][0]][count_locate[m % 6][1]] = " "
        # 先将六次之前的棋子清除
    #   count_list[a] = player
    count_locate[m % 6][0] = row
    count_locate[m % 6][1] = down
    # 再将第a次下棋的位置和棋子存起来


def ask_final():
    choose_bool = input("挖去，游戏结束哩，你还要继续玩吗（输入yes/no）：")
    if choose_bool == "yes":
        return True
    elif choose_bool == "no":
        print("下次再见bro！")
        return False
    else:
        print("bro请输入yes或者no，检查一下空格等符号问题")
        ask_final()


# 主函数
round_player = int(0)  # 记录回合数
player = "O"
print_pan(board)
while True:
    if round_player % 2 == 0:  # 判断到谁的回合
        player = "O"
    else:
        player = "X"

    position = input(f"请player{player}输入你要选择的位置1～9：")
    if position.isdigit():
        position_int = int(position)
        count_list[round_player % 6] = position_int
    else:
        print("请你输入一个数字，bro")
        continue
    row = int((position_int - 1) // 3)  # 记录坐标
    down = int((position_int - 1) % 3)

    if position_int > 9 or position_int < 1:
        print("厚礼蟹！你输入的位置超出棋盘空间啦，换一个地方吧")
        continue
    if board[row][down] == " ":
        board[row][down] = player
        round_player += 1
    else:
        print("这里已经被占用啦，换一个位置吧")
        continue
    count(round_player, count_list[round_player % 6])
    print_pan(board)
    if check(board):
        # print_pan(board)
        print(f"恭喜player{player}赢了")
        if ask_final():
            continue
        else:
            break