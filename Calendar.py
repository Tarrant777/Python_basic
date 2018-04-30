 # encoding: utf-8
year=input("Plz input year:")
month=input("Plz input month:")
year=int(year)
month=int(month)
leapyeartimes=year//4-year//100+year//400
monthday=[31,28,31,30,31,30,31,31,30,31,30,31]
if year%400 == 0 :
    monthday[1]=29
    leapyeartimes=leapyeartimes-1
elif year%100 == 0:
    monthday[1]=28
elif year%4 == 0 :
    monthday[1]=29
    leapyeartimes=leapyeartimes-1
else:
    monthday[1]=28

thisyeardays=sum(monthday[0:month-1])
totaldays=(year-1)*365+leapyeartimes+thisyeardays
monthfirst=(totaldays+1)%7
print(year,"年",month,"月")
outputday=[" S"," M"," T"," W"," T"," F"," S"]
if monthfirst == 0:
    j=0
else:
    for j in range(1,monthfirst+1):
        outputday.append("  ")
for i in range(1,monthday[month-1]+1):
    outputday.append(i)
    if i < 10:
        outputday[i-1+j+7]=" "+str(outputday[i-1+j+7])
    else:
        outputday[i-1+j+7]=str(outputday[i-1+j+7])
"""
for i in range(0,6):
    print outputday[i*7:7*(i+1)]
"""
for k in range(0,14):
    outputday.append("  ")
for i in range(0,7):
    sunday=outputday[i*7]
    monday=outputday[i*7+1]
    tuesday=outputday[i*7+2]
    wednesday=outputday[i*7+3]
    thursday=outputday[i*7+4]
    friday=outputday[i*7+5]
    saturday=outputday[i*7+6]
    print(sunday,monday,tuesday,wednesday,thursday,friday,saturday)
 

