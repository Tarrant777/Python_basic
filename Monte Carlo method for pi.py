# encoding: utf-8
import random
import time
import math
import matplotlib.pyplot as plt

total = 10 ** 2
inside = 0
print(time.strftime("%H:%M:%S"))
plt.title("Monte Carlo method for pi")
plt.ylabel("y")
plt.xlim(0)
plt.ylim(0)
x1 = [0]
y1 = []
R = 1000

for j in range(0, R):
    x1.append(float(1 / R) + x1[j])
    y1.append(math.sqrt(1.0 - (x1[j] ** 2)))
del x1[R]
plt.plot(x1, y1)

x = []
y = []

for i in range(total):
    x.append(random.uniform(0, 1))
    y.append(random.uniform(0, 1))
    if x[i] ** 2 + y[i] ** 2 <= 1:
        inside = inside + 1
plt.scatter(x, y, s=1, c="r")
pi = float(inside * 4.0) / float(total)
plt.xlabel("X      " + "Total Point=" + str(total) + "   pi=" + str(pi))
print(time.strftime("%H:%M:%S"))
print(float(inside), float(total), pi)
print(math.pi)
# 讓x y軸等長
ax = plt.gca()
ax.set_aspect(1)

plt.show()
