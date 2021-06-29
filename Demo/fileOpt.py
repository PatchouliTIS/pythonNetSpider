import os
# 覆盖写w   追加a
f = open('text.txt', 'w')

f.write("Rangers Lead the Way\n")
f.close()


# 读数据r   ~.read()中表明读数据的字节长度,默认是读出所有数据

# ~.read()需要用一个左值来接收

f = open('text.txt', 'r')
context = f.read(5)     # 字节

print("-" * 30)
print(context)

f.close()

# 按照记录行读取文件

f = open('text.txt', 'a')
f.write("YJSDJJDA\n")
f.write("12312124\n")
f.close()


f = open('text.txt', 'r')
linesight = f.readline()    # 字符串
print("1:%s" % linesight)   # 此时指针移动到下一行
f.close()

f = open('text.txt', 'r')
allLines = f.readlines()    # 字符串列表List
i = 1
for str in allLines:
    print("%d:%s" % (i, str))
    i += 1
f.close()

# 调入OS库来实现

# 1. 重命名

os.rename("text.txt", "tar.txt")

# 2. 删除文件
os.remove("tar.txt")

# 3. 创建文件夹
os.mkdir("掌机")
