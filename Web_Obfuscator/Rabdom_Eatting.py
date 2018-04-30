# encoding: utf-8
import random

food_list = ["我家牛排", "手沖牛肉麵", "乾意麵+干連肉", "乾意麵", "肉燥飯+小菜", "肉燥飯", "爭鮮", "趙哥牛肉麵", "干連麵"]

x = len(food_list)
print(x)
y = random.randint(1, x)
print(y-1)
print(food_list[y-1])
