### HW05 Prob.1
# prime_number.py
# Author: Chiao-Yin Teng

### Problem description
# A prime number is a natural number greater than 1
# that has no positive divisors other than 1 and itself.
# Enter a positive integer, the program will judge whether
# the integer is a prime number or not.

### Skills and functions
# input(), int(), arithmetic expression
# if, for, format()

### Example IO (cmd prompt: "dengqiaoyin$ > ")
# dengqiaoyin$ > python3 prime_number.py
# please enter a positive integer: 97
# 97 is a prime number.
# dengqiaoyin$ > python3 prime_number.py
# please enter a positive integer: 121
# 121 is not a prime number.

### Reference solution
n = int(input('please enter a positive integer: '))
if n == 1:
    print('{} is not a prime number.'.format(n))
if n == 2:
    print('{} is a prime number.'.format(n))
for i in range(2,n):
    if n % i == 0:
        print('{} is not a prime number.'.format(n))
        break
    if i == n-1:
        print('{} is a prime number.'.format(n))
