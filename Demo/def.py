# 打印横线
def printLine():
    print("-" * 30)


printLine()

# 全局与局部变量
# 在函数外边定义的变量叫做全局变量
# 如果在函数中修改全局变量，那么就需要使用global 进行声明，否则出错
a = 10


def aMend():
    global a
    a += 1
    print(a)


print(a)
