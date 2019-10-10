'''
Created on 2019/10/09

@author: t17cs050
'''
import random

num = random.randint(1, 3)
num2 = "0"
numB = 0

handA = "String"
handB = 'string'

print("じゃんけんシミュレート")
print("1~3の数字を入力！")
num2 = input()
numB = int(num2)

if num == 1:
    handA = "グー"
elif num == 2:
    handA = "チョキ"
elif num == 3:
    handA = "パー"
    
if numB == 1:
    handB = "グー"
elif numB == 2:
    handB = "チョキ"
elif numB == 3:
    handB = "パー"
    
print("Aの手：", handA, "VS Bの手：", handB)

if num == numB:
    print("引き分け")
elif (num == 1 and numB == 2) or (num == 2 and numB == 3) or (num == 3 and numB == 1):
    print("Aの勝ち")
elif (numB == 1 and num == 2) or (numB == 2 and num == 3) or (numB == 3 and num == 1):
    print("Bの勝ち")