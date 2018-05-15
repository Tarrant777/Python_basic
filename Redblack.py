# encoding: utf-8
import random

i

randomtimes = 100
# 隨機次數
numbers = 1
# 樣本數
d = {}
# 產生對應字典

Total_property = 0
Bet = [1, 3, 9, 27, 81, 243, 729]  # 下注值

Result = []  # 紅黑輸贏結果

for j in range(0, numbers + 1):
    Result = []  # 歸零
    for i in range(0, randomtimes + 1):
        a = random.randint(0, 999)
        if a <= 499:

            Result.append(1)
        else:
            Result.append(0)
    d[j] = Result  # 把j號樣本放入字典


