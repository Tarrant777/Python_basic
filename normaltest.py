 # encoding: utf-8
import random
times=100
x = open('x.txt', 'r+')
x.write('Its just test\n')
"""
for step in range(times):
    if random.randint(0,99) >50:
        x.write(str(x[step]+1))
    else:
        x.write(str(x[step]-1))
"""
