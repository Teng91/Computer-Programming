#讀檔案
fobj = open('words.txt','r')
all_lines = fobj.readlines()
#使用者輸入字元
letter = input('enter a letter (a to z): ')
#記錄head或tail
count_head = 0
count_tail = 0
#判斷輸入字元是否為第一個或最後一個
for i in range(len(all_lines)):
    if letter == all_lines[i][0]:
        count_head += 1
    if letter == all_lines[i][-2]:
        count_tail += 1
print(letter,'as head:',count_head,'times,','as tail',count_tail,'times.')

