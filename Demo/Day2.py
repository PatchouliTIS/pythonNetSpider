# 循环 for while
'''
a = ["aa", "bb", "cc", "dd"]


for x in range(len(a)):
    print(x, end="\t")

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("100以内的和是：%d" % sum)
'''

# 在Python中，while可以和else配合使用，输出一次

i = 0
while i < 10:
    i += 1
    print("*"*30)       # 多个重复元素的输出可以直接乘以数值
    if i % 5 == 0:
        break
    print(i)


# 字符串
# word 单引号'...'
# sentence 双引号"..."
# paragraph 三引号"""..."""
# Python中输入的数据默认作为string存储


# 字符串的访问
str = "YJSP"

print(str[0])
print(str[0:2])
print(str[0:4:2])
print(str[:5])      # 可以超过字符串本身的长度
# [起始位置(默认为0):结束位置(不包含,不输入则默认到结尾):每步进位值(默认1)]

print(str + "sukitsu!")
print(str * 3)      # 多次打印

print(r"hello\nchengdu")    # r开头表示无视反斜杠\ 直接全部输出

print("%d * %d = %d"%(i, j, i*j))
# 常用的字符串API
# byte.decode(encoding="utf-8", errors="strict")    解码方式utf-8
# encode(encoding="utf-8", errors="strict")     编码方式
# errors="strict" 指明如果出错则报告ValueError异常，如果是"ignore"或"replace"则无视

# isalnum()     判断是否是全数字或者字母
# isalpha()     判断是否是全字母
# isdigit()     纯数字
# isnumeric()   数值字符

# len(string)

# lstrip()      去掉左边空格
# rstrip()      去掉右边空格
# split(str=" ", num=...)
