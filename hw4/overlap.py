#enter bounds
l1 = int(input('enter the lower bound of interval 1: '))
u1 = int(input('enter the upper bound of interval 1: '))
l2 = int(input('enter the lower bound of interval 2: '))
u2 = int(input('enter the upper bound of interval 2: '))
if max(l1,l2) < min(u1,u2):
    print('[{},{}] and [{},{}] overlap.'.format(l1,u1,l2,u2))
else:
    print("[{},{}] and [{},{}] don't overlap.".format(l1,u1,l2,u2))
