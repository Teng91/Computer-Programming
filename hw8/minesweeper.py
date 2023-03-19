### HW08 Prob.1
# minesweeper.py
# Author: Chiao-Yin Teng

### Problem description
# Minesweeper is a popular game where the user
# has to find the mines using numeric hints that
# indicate how many mines are directly in a square
# (horizontally, vertically, diagonally).
# Where the empty spaces are indicated by "·",
# and the mines are indicated by "*". Calaulate
# the number of mines in each nine-square division.

### Skills and functions
# arithmetic expression
# if, for, list, str, def

### Example IO (cmd prompt: "dengqiaoyin$ > ")
# dengqiaoyin$ > python3 minesweeper.py
# printBoard(mineCount(['·*·*·',
#                       '··*··',
#                       '*·*·*',
#                       '··*··',
#                       '·····']))
# +-----+
# |1*3*1|
# |24*42|
# |*4*4*|
# |13*31|
# |·111·|
# +-----+

### Reference solution
def printBoard(board):
    str1 = "+"
    print(str1+"-"*len(board[0])+str1)
    str2 = "|"
    for i in range(len(board)):
        print(str2+str(board[i])+str2)
    print(str1+"-"*len(board[0])+str1)

def mineCount(board):
    height = len(board)
    width = len(board[0])
    ans = []
    ans_str = ""
    for i in range(len(board)): #從左上開始，垂直方向
        for j in range(len(board[i])): #從左上開始，水平方向
            count = 0
            if board[i][j]!="*":
                if i-1>=0: #上
                    if board[i-1][j] == "*":
                        count+=1
                if i+1<height: #下
                    if board[i+1][j] == "*":
                        count+=1
                if j-1>=0: #左
                    if board[i][j-1] == "*":
                        count+=1
                if j+1<width: #右
                    if board[i][j+1] == "*":
                        count+=1
                if i-1>=0 and j-1>=0: #左上
                    if board[i-1][j-1] == "*":
                        count+=1
                if i+1<height and j+1<width: #右下
                    if board[i+1][j+1] == "*":
                        count+=1
                if i-1>=0 and j+1<width: #左下
                    if board[i-1][j+1] == "*":
                        count+=1
                if i+1<height and j-1>=0: #右上
                    if board[i+1][j-1] == "*":
                        count+=1
                if count==0:
                    ans_str += board[i][j]
                else:
                    ans_str += str(count)
            elif board[i][j]=="*": #如果位置上剛好是*字，保留*字到新的ans_list
                ans_str += "*"
        ans.append(ans_str)
        ans_str = ""
    return ans

printBoard(mineCount(['·*·*·',
                      '··*··',
                      '*·*·*',
                      '··*··',
                      '·····']))
