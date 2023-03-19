# count_char.py
string = input('enter a string: ')
target = input('enter the character to count: ')

count = 0 #起始條件
for char in string:
    if char == target:
        count += 1
if count == 1:
    print(
        "\n'%s' appears %d time in '%s'." %
        (target,count,string)
    )
else:
    print(
        "\n'%s' appears %d times in '%s'." %
        (target,count,string)
    )
