for number in range(100,1000,1):
    a = number // 100 #百位數
    b = number // 10 % 10 #十位數
    c = number % 10 #個位數
    if number == a**3 + b**3 + c**3:
        print("{}^3 + {}^3 + {}^3 = {}".format(a,b,c,number))
