number = int(input('enter a positive integer: '))
# initial guess (x/2)
x = number/2
print('guess 0 :','%.10f'%x)
# ten guesses(from 1 to 10)
for i in range(1,10):
    x = 0.5*(x+number/x)
    print('guess',i,': %.10f'%x)
