# encoding: utf-8
import matplotlib.pyplot as plt
import math

n = 120
h = 0.05

x = 1.0
k1 = []
k2 = []
k3 = []

for i in range(1, n):
    x0 = x
    k1.append(-x0)
    k2.append(-(x0 + (h * k1) / 3.0))
