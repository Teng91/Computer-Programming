#generate the lists of random integers
import random
low = 0
high = 100
count = 100
numbers = random.choices(range(low,high+1),k=count)
#find maximum, minimum, sum (起始條件)
maximum = low 
minimum = high
sum = 0
#for迴圈 遇到更大更小值就取代
for n in numbers:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n
    sum += n
#show statistics
print('minimum: %d' % minimum)
print('maximum: %d' % maximum)
print('average: %.2f' % (sum/count))
