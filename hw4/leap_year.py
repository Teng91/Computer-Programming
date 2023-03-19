### HW04 Prob.1
# leap_year.py
# Author: Chiao-Yin Teng

### Problem description
# A year is a leap year if y is divisible by 4,
# but not divisible by 100 or y is divisible by 400.
# The user needs to enter a vaild year, and then
# the result should be printed.

### Skills and functions
# arithmetic expression, input(), int()
# if, else expression

### Example IO (cmd prompt: "dengqiaoyin$ > ")
# dengqiaoyin$ > python3 leap_year.py
# Please insert a valid year: 2000
# The year is a leap year.
# dengqiaoyin$ > python3 leap_year.py
# Please insert a valid year: 1900
# The year is not a leap year.

### Reference solution
y = int(input("Please insert a valid year: "))
if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
