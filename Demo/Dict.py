# 字典  dict
# HashMap同类

info = {"name": "Ranger", "age": 18}    # 注意与C++中键值插入操作的区别
# c++ {"bane", 18},{"...", ...}
print(info["name"])     # 输出Ranger
# 直接访问会报错，不健壮


# 推荐使用~.get(key,default) 若没有找到则输出default
print(info.get("gender", "m"))

# 查询 1
# 以列表List的形式返回dict里的键
listVAL = info.values()     # 以列表List的形式返回dict里的键值

# 查询 2
for A in info.keys():
    print(A)

# 遍历所有的键与键值
for key, value in info.items():
    print("key=%s,value=%s" % (key, value))

# 或者不输入参数,自动遍历所有参数
print(info.values())
print(info.items())

# 将其他元素强转为字典
convert = dict([(1, 2), (3, 4)])

# 合并字典,将convert中的键值队更新到info中去
info.update(convert)

# 将两个List合并为字典，第一个为key，第二个为val
List1 = [1, 2, 3, 4]
List2 = ["张三"]
dict2 = (zip(List1, List2))
