# encoding: utf-8]
import matplotlib
import matplotlib.pyplot as plt

dr = 0.01
x = [0.3]
dt = 1
t = 200
y = [0]

plt.title("Logistic map")
plt.xlim(0)
plt.ylim(0)
plt.ylabel("X")

for i in range(0, int(4 / dr)):
    print(i * dr)
    y = [0]
    x = [0.3]
    for n in range(0, int(t / dt)):
        x.append((i * dr) * x[n] * (1.0 - x[n]))
        y.append(y[n] + dt)
    plt.plot(y, x)
    plt.ylabel("X")
    plt.xlabel("t      r=" + str(i * dr))
    # plt.savefig("test"+str(i)+".png")
    plt.show()
