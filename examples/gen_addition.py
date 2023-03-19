import estimate_carry
import random
count = 10
for i in range(10):
    x = random.randint(1000,9999)
    y = random.randint(1000,9999)
    est_carry = estimate_carry.estimate_carry(x,y)
    print('Addition of %d and %d incurs roughly %d carries.'% (x,y,est_carry))
