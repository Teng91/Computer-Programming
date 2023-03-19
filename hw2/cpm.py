import cmath
#get 3 numbers
a = float(input('enter loan amount: '))
b = float(input('enter annual interset rate (%): '))
c = float(input('enter length of term (years): '))
#counting
d = (a*(b/12/100))/(1-(1+(b/100/12))**(-c*12))
#print result
print('monthly repay = ',d)
