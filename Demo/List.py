# List 列表
# 与数组类似，但可以存储多个不同数据类型的元素


# 基本操作
a = ["a", "b", "c", "a", "d", "e"]
# 访问
x = a[-1]
y = a[len(a)-1]       # 两者等价  可以用负号进行倒序的访问


# 查
target = input("请输入你的查找内容：")
if target in a:
    x = a.index(target, 0, len(a))        # ~.index(str, start, end) ??~?б????±?start????end(??????)??Χ?????str??????
    print("存在与数组中，其下标为：%d" % x)
else:
    print("不存在于数组中")


# 排序
a.reverse()     # 反转
a.sort()
a.sort(reverse=True)      # 降序

# 列表的嵌套 也就是二维数组
Office = [[], [], []]   # 三个空列表组成的一个列表


# 用枚举类型enumerate()遍历并输出列表中的值中的值
myList = ["a", "b", "c", "d"]       # 列表

for i, x in enumerate(myList):
    print(i + 1, x)
