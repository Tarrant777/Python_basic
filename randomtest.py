 # encoding: utf-8
import random
import time
import math
total=10**10
inside=0
print (time.strftime("%H:%M:%S"))
for i in range(total):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if x**2+y**2 <= 1:
             inside=inside+1
  
print (time.strftime("%H:%M:%S"))
print (float(inside),float(total),(float(inside*4.0)/float(total)))
print (math.pi)




