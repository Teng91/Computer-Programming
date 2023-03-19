### HW03 Prob.1
# Trapezoid_area.py
# Author: Chiao-Yin Teng

### Problem description
# Write a program that asks the user
# enter the upper bottom, lower bottom and height,
# and then prints the Trapezoid area. 
# The area should be printed with 2 decimal digits.

### Skills and functions
# arithmetic expression, assignment, string formatting
# float(), input()

### Example IO (cmd prompt: "dengqiaoyin$ > ")
# dengqiaoyin$ > python3 Trapezoid_area.py
# Enter the upper bottom: 2
# Enter the lower bottom: 2
# Enter the height: 2
# The Trapezoid area is 4.00

### Reference solution
import math
upper = float(input('Enter the upper bottom: '))
lower = float(input('Enter the lower bottom: '))
height = float(input('Enter the height: '))
area = (upper+lower)*height/2
print('The Trapezoid area is %.2f' % area)
