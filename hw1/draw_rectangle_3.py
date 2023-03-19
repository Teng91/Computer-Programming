w = int(input('enter the width: '))
h = int(input('enter the height: '))
for i in range(w*h):
    print(i,end='\t')
    if (i+1) % h == 0:
        print(end="\n")
