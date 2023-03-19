w = int(input('enter the width: '))
h = int(input('enter the height: '))
for i in range(0,h):
    if i == 0 or i == h-1:
        print('*'*w)
    else:
        print('*'+' '*(w-2)+'*')
