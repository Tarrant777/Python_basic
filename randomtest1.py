# encoding: utf-8
import random
import matplotlib.pyplot as plt

randomtimes = 100
# 隨機次數
numbers = 100000
# 樣本數
passlist = [0]
# 歷程
d = {}
# 產生對應字典
x = [0]

for j in range(0, numbers):
    passlist = [0]  # 歸零
    x = [0]
    for i in range(0, randomtimes):
        a = random.randint(0, 999)
        x.append(x[i] + 1)
        if a <= 499:
            passlist.append(passlist[i] + 0.5)
        else:
            passlist.append(passlist[i] - 0.5)
    d[j] = passlist  # 把j號樣本放入字典

"""各樣本軌跡圖
plt.subplot(211)
for n in range(0, numbers):
    plt.plot(x, d[n])
plt.xlim(0)
"""


x = []  # 重設乾淨的x軸
t = -float(randomtimes + 1) / 2  # 級距初始值
y = [-int((randomtimes + 1) / 2)]  # y軸初始值
# print("t=", t, "y=", y)

"""統計各區間x軸的值"""
for k in range(0, randomtimes + 1):
    x.append(0)
    for n in range(0, numbers):
        if float(d[n][randomtimes]) < (t + 1) and float(d[n][randomtimes]) > t:
            x[k] = x[k] + 1
    t = t + 1.0
    y.append(y[k] + 1)
del y[(randomtimes + 1)]  # y會多一個,刪掉它!
# print("t=", t)
# print("y=", y, "len=", len(y))
# print("x=", x, "len=", len(x))
#plt.subplot(212)
plt.plot(x, y)
plt.xlim(0)

plt.show()
