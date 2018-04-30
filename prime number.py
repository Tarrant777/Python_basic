import time
n=10**1
prime_number=[2]
print (time.strftime("%H:%M:%S"))
for i in range(3,n+1,2):
    x=len(prime_number)
    for j in range(x):
        if i%prime_number[j] == 0:
            break
        else:
            continue
    if j == (x-1):
        prime_number.append(i)
print (time.strftime("%H:%M:%S"))
            
        
