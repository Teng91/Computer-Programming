### HW07 Prob.1
# tic_tac_toe.py
# Author: Chiao-Yin Teng

### Problem description
# Given a 3x3 matrix of a tic-tac-toe game,
# define a function that returns whether
# the game is "X" or "O" win, otherwise "Draw".
# "X" and "O" represent themselves on the matrix,
# and "E" represents an empty space.

### Skills and functions
# arithmetic expression
# if, for, list, def

### Example IO (cmd prompt: "dengqiaoyin$ > ")
# dengqiaoyin$ > python3 tic_tac_toe.py
# tic_tac_toe([["X", "O", "X"],["O", "X", "O"],["O", "X", "X"]])
# 'X'
# tic_tac_toe([["O", "O", "O"],["O", "X", "X"],["E", "X", "X"]])
# 'O'
# tic_tac_toe([["X", "X", "O"],["O", "O", "X"],["X", "X", "O"]])
# 'Draw'

### Reference solution
# 定義主函式
def tic_tac_toe(A):
    n = 3
    # 定義獲勝條件
    def win(pattern):
        # 判斷True和False的數量，數量等於3代表連線成功
        B = [[A[i][j] == pattern for j in range(n)] for i in range(n)]
        for i in range(n):
            if sum(B[i][j] for j in range(n)) == n: #列
                return True
            if sum(B[j][i] for j in range(n)) == n: #行
                return True
            if sum(B[i][i] for i in range(n)) == n: #左上到右下
                return True
            if sum(B[i][n-1-i] for i in range(n)) == n: #右上到左下
                return True
        return False
    # 判斷"X","O"獲勝，否則回傳"Draw"
    for pattern in ["X","O"]:
        if win(pattern):
            return pattern
    return "Draw"

# test
print(tic_tac_toe([["X", "O", "X"],["O", "X", "O"],["O", "X", "X"]]))
print(tic_tac_toe([["O", "O", "O"],["O", "X", "X"],["E", "X", "X"]]))
print(tic_tac_toe([["X", "X", "O"],["O", "O", "X"],["X", "X", "O"]]))
