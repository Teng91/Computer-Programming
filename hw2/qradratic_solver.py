import cmath
#introduction
print('***** Welcome to Quadratic Equation Solver *****')
print('      ax^2 + bx + c = 0')
#get 3 numbers
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))
#discriminant
d = b**2-4*a*c
#solve roots
root_1 = (-b+cmath.sqrt(d))/(2*a)
root_2 = (-b-cmath.sqrt(d))/(2*a)
#print result
print('The two roots are:\n{0}\n{1}'.format(root_1,root_2))
