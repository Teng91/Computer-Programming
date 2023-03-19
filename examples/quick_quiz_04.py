# quick_quiz_04.py
# A quiz of addition/subtraction problems.
# The student specifies the number of problems.
# Both operands in [10,99] and the answer must be >= 0.
# ask for problem count
prob_count = int(input('enter the number of problems: '))
# start the quiz
import random
correct_count = 0
for i in range(prob_count):
    op1 = random.randint(10,99)
    op2 = random.randint(10,99)
    operator = random.choice('+-')
    if operator == '-':
        if op1 < op2:
            op1,op2 = op2,op1
        answer = op1 - op2
    else:
        answer = op1 + op2
    # prepare the problem
    problem = '%d %s %d =' % (op1,operator,op2)
    # show problem and get answer
    response = int(input('\nProb. %d: %s ' % (i+1,problem)))
    # show message
    if response == answer:
        print('\tGood job!')
        correct_count += 1
    else:
        print('\t%s %d, not %d.' % (problem,answer,response))
# show final grade
print('\nFinal score: %.2f.' % (correct_count/prob_count*100))
