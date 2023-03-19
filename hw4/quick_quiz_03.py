# generate operands and operators
import random
op1 = random.randint(10,99)
op2 = random.randint(10,99)
operator = random.choice('+-')
# prepare the problem
if operator == '+' or (operator == '-' and op1 > op2):
    problem = '%d %s %d = ' % (op1,operator,op2)
else:
    problem = '%d %s %d = ' % (op2,operator,op1)
# get answer
response = int(input(problem))
if operator == '+' or (operator == '-' and op1 > op2):
    answer = op1 + op2
    if response == answer:
        print('Good job!')
    else:
        print('%d %s %d = %d, not %d.' % (op1,operator,op2,answer,response))
else:
    answer = op2 - op1
    if response == answer:
        print('Good job!')
    else:
        print('%d %s %d = %d, not %d.' % (op2,operator,op1,answer,response))
