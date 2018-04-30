 # encoding: utf-8
year=raw_input("請輸入年份:")
month=raw_input("請輸入月份:")
year=int(year)
month=int(month)
leapyeartimes=year/4-year/100+year/400
monthday=[31,28,31,30,31,30,31,31,30,31,30,31]
if year%4 == 0 and year%400 != 0:
    monthday[1]=29
    leapyeartimes=leapyeartimes-1
else:
    monthday[1]=28
thisyeardays=sum(monthday[0:month-1])
totaldays=(year-1)*365+leapyeartimes+thisyeardays
monthfirst=(totaldays+1)%7
print year,"年",month,"月"
outputday=[" S"," M"," T"," W"," T"," F"," S"]
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
for i in range(0,6):
    outputday.append("  ")
    print outputday[i*7],outputday[i*7+1],outputday[i*7+2],outputday[i*7+3],outputday[i*7+4],outputday[i*7+5],outputday[i*7+6]


