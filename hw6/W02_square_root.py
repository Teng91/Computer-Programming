number = int(input('enter a positive integer: '))
# initial guess (x/2)
x = number/2
print('guess 0 :','%.10f'%x)
error = abs(x**2-number)
i = 1
while error > 1e-8:
    x = 0.5*(x+number/x)
    print('guess',i,': %.10f'%x)
    i += 1
    error = abs(x**2-number)
print('error =',error)
