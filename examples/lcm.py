a_org = int(input('enter a: '))
b_org = int(input('enter b: '))
a,b = a_org,b_org
while a != b:
    if a < b:
        a = a + a_org
    else: #因為while已經比過一次a!=b
        b = b + b_org
ans = a
print('lcm({},{}) = {}'.format(a_org,b_org,ans))
