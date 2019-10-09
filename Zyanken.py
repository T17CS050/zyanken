'''
Created on 2019/10/09

@author: t17cs050
'''
import random

num = random.randint(1, 3)
num2 = random.randint(1, 3)
print("じゃんけんシミュレート")

if num == num2:
    print("引き分け")
elif num < num2:
    print("勝ち")
elif num > num2:
    print("負け")