# encoding: utf-8
import random


randomtimes = 100
# 隨機次數
numbers = 1
# 樣本數
d = {}
# 產生對應字典

payback = 0.95

Total_property = 0
Bet = [1, 3, 9, 27, 81, 243, 729]  # 下注值

Result = []  # 紅黑輸贏結果


def game()


for j in range(0, numbers + 1):
    Result = []  # 歸零
    for i in range(0, randomtimes + 1):

        a = random.randint(0, 999)
        if a <= 499:
            Result.append(1)
        else:
            Result.append(0)
        if i > 3 and Result(i - 1) == Result(i - 2) and Result(i - 1) == Result(i - 3):
            if Result(i-1)==1 and Result(i)== 1:


    d[j] = Result  # 把j號樣本放入字典
