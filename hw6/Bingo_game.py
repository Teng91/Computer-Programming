### HW06 Prob.1
# Bingo_game.py
# Author: Chiao-Yin Teng

### Problem description
# A 4*4 bingo game, user needs to enter the bingo number,
# the number which has been chosen will turn out to be "*",
# until covers four "*" in a straight line, no matter they
# are "ㄧ", "|", "\" or "/", print "Bingo!" and print all
# the numbers that user entered.

### Skills and functions
# input(), int(), arithmetic expression, random
# if, for, while, list, list.append()

### Example IO (cmd prompt: "dengqiaoyin$ > ")
# dengqiaoyin$ > python3 Bingo_game.py
# 5   6   1   11
# 7   8   3   13
# 4   2   12  10
# 16  14  15  9
#中獎號碼：5
# *   6   1   11
# 7   8   3   13
# 4   2   12  10
# 16  14  15  9
#中獎號碼：8
# *   6   1   11
# 7   *   3   13
# 4   2   12  10
# 16  14  15  9
#中獎號碼：12
# *   6   1   11
# 7   *   3   13
# 4   2   *   10
# 16  14  15  9
#中獎號碼：9
# *   6   1   11
# 7   *   3   13
# 4   2   *   10
# 16  14  15  *
# Bingo!
# ['5', '8', '12', '9']

### Reference solution
import random
number_all = [] #儲存賓果盤
number = [] #儲存中獎數字
line = [] #儲存每條線尚未中獎的數字個數
Bingo = 1 #判斷是否連線的變數
#將數字1到16隨機放入賓果盤
for i in range(1,17):
    number_all.append(i)
random.shuffle(number_all)
#印出賓果盤
for j in range(16):
    print(number_all[j], end="\t")
    #每4個數字換行
    if j%4 ==3:
        print("\n")
#將每條線尚未中獎的數字個數預設為4
for k in range(10):
    line.append(4)
#主程式開始執行
while(Bingo != 0): #while迴圈執行條件
    choice = int(input("中獎號碼：")) #使用者開始輸入中獎號碼
    number.append(choice) #記錄每次中獎號碼
    print() #換行
    #若中獎號碼在某直排
    for check_column in range(4):
        if(number_all.index(int(choice)) % 4 == check_column):
                line[check_column] -= 1 #該條線尚未中獎的數字個數-1
    #若中獎號碼在某橫排
    for check_row in range(4):
        if(number_all.index(int(choice)) // 4 == check_row):
                line[check_row+4] -= 1 #該條線尚未中獎的數字個數-1
    #若中獎號碼在斜排
    if(number_all.index(int(choice)) == 0):
        line[8] -= 1 #該條線尚未中獎的數字個數-1
    elif(number_all.index(int(choice)) % 5 == 0): #判斷左上到右下
        line[8] -= 1 #該條線尚未中獎的數字個數-1
    elif(number_all.index(int(choice)) % 3 == 0): #判斷右上到左下
        line[9] -= 1 #該條線尚未中獎的數字個數-1
    #中獎號碼改成"*"符號
    number_all[number_all.index(int(choice))] = "*"
    #印出新的賓果盤
    for j in range(16):
        print(number_all[j], end="\t")
        #每4個數字換行
        if j%4 ==3:
            print("\n")
    #當該條線尚未中獎的數字個數為0時，Bingo==0，結束迴圈
    for l in range(10):
        Bingo *= line[l]
print("Bingo!")
print(number) #將所有中獎號碼印出來
