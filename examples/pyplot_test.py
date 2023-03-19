import matplotlib.pyplot as plt
#總共幾條線
x, x_10, x_square = [], [], []
#定義每條線所代表的數學方程式
for n in range(10):
    x.append(n)
    x_10.append(10*n)
    x_square.append(n**2)
#給定label的值，存到legend裡面
plt.plot(x, x, 'x--b', label='x') #marker = 'x', line = '--', color = 'b'
plt.plot(x, x_10, 'or', label='10x') #marker = 'o', color = 'r'
plt.plot(x, x_square, '^-g', label='x^2') #marker = '^', line = '-', color = 'g'
#給定x,y座標範圍(先x後y)
plt.axis([0,10,0,120])
#給定座標軸
plt.xlabel('x')
plt.ylabel('y')
#給定表名與圖例
plt.title("test")
plt.legend()
plt.show() #最後一定要show()才會顯示圖表
