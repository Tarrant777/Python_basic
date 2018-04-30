# encoding: utf-8
import random
import matplotlib.pyplot as plt

randomtimes = 10
# 隨機次數
numbers = 10
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
        a = random.randint(0, 99)
        x.append(x[i] + 1)
        if a <= 49:
            passlist.append(passlist[i] + 1)
        else:
            passlist.append(passlist[i] - 1)
    d[j] = passlist  # 把j號樣本放入字典

print("各樣本軌跡")
for n in range(0, numbers):
    plt.plot(x, d[n])

print('各樣本結果')
# 創造級距
# for k in range(0, numbers+1):
# x歸零
x = []
t = -float(numbers + 1)
for k in range(0, numbers + 1):
    x.append(0)
    for n in range(0, numbers):
        if float(d[n][randomtimes]) < t+1 and float(d[n][randomtimes]) > t:
            x[k] = x[k] + 1
    t = t+1.0

print(x)
