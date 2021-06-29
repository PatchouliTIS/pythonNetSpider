'''

score = int(input("请输入你的分数："))

if score >= 90:     # 代表分数等级
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("DEAD")
'''


import random

x = random.randint(0, 2)       # 0剪刀   1石头    2布

y = int(input("来决斗吧！\n"))

if x == 1:
    sa = "石头"
elif x == 0:
    sa = "剪刀"
elif x == 2:
    sa = "布"

if x - y == 1 or x == 0 and y == 2:
    print("你输了！我出的是%s " % sa)
elif y - x == 1 or y == 0 and x == 2:
    print("你赢了！我出的是%s " % sa)
else:
    print("书你吗呢")
