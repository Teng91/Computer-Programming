### HW09 Prob.1
# Counting_Characters.py
# Author: Chiao-Yin Teng

### Problem description
# Write a function that takes a string S and
# returns a dictionary which contains number
# of occurrences of each character occurring
# and number of characters in string S.

### Skills and functions
# string processing, 
# if, for, dictionary

### Example IO (cmd prompt: "dengqiaoyin$ > ")
# dengqiaoyin$ > python3 Counting_Characters.py
# print(count_char('National Taiwan University'))
# ({'n': 4, 'a': 4, 't': 3, 'i': 4, 'o': 1, 'l': 1, 'w': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 'y': 1}, 24)
# print(count_char('Computer Programming'))
# ({'c': 1, 'o': 2, 'm': 3, 'p': 2, 'u': 1, 't': 1, 'e': 1, 'r': 3, 'g': 2, 'a': 1, 'i': 1, 'n': 1}, 19)

### Reference solution
import re
def count_char(S):
    # 去掉空格並轉換成小寫
    s = re.sub(r"\s+", "", S.lower())
    number = 0 # 計算字母總數
    count = {} # 計算字母種類以及出現次數
    for i in s:
        if i in count:
            count[i] += 1
            number += 1
        else:
            count[i] = 1
            number += 1
    return count, number

print(count_char('Computer Programming'))
