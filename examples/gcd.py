a_org = int(input('enter a: '))
b_org = int(input('enter b: '))
a,b = a_org,b_org
while a != b:
    if a > b:
        a = a - b
    else: #因為while已經比過一次a!=b
        b = b - a
ans = a
print('gcd({},{}) = {}'.format(a_org,b_org,ans))
