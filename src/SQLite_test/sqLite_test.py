# -*- coding: utf-8 -*-
# sqLite_test.py
# @author Patchouli Tisa
# @description RLTW
# @created 2021-07-10T12:22:26.332Z+08:00
# @last-modified 2021-07-10T16:11:09.467Z+08:00
#
import sqlite3

# 打开或创建一个数据库（位置）  生成一个连接对象conn
conn = sqlite3.connect(".\\src\\SQLite_test\\test.db")
#          游标
csr = conn.cursor()

clr_sql = '''
    SELECT count(*) FROM sqlite_master WHERE type="table" AND name = "stu_score"
'''
cnt = csr.execute(clr_sql)

if cnt == 0:
    # python中'''..'''表示一段字符，保持输入格式
    csr.execute('''CREATE TABLE IF NOT EXISTS stu_score
                    (id int primary key not null,
                    sort int,
                    name text,
                    price real)''')
    # 1. 插入数据
    # 单独插入
    csr.execute('''INSERT INTO stu_score VALUES
                (1,1,"computer science",77)''')

    # 批量插入
    stu_score = [
        (2, 1, "computer science", 79),
        (3, 3, "python science", 80),
        (4, 4, "stm32 science", 90),
    ]
    # 多段执行
    csr.executemany('INSERT INTO stu_score VALUES(?,?,?,?)', stu_score)

    # 提交  生效sql语句
    conn.commit()

    conn.close()

    print("Opened Database successfully")
else:
    print("Database already exists")

# 2. 查询数据

conn = sqlite3.connect(".\\src\\SQLite_test\\test.db")
csr = conn.cursor()

sql = "SELECT * FROM stu_score WHERE sort==2"

content = csr.execute(sql)

for item in content:
    print("ID = {} \t SORT = {} \t NAME = {} \t PRICE = {} \t".format(item[0], item[1], item[2], item[3]))
