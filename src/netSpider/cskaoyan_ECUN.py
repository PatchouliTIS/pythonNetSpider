from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
# import requests   作用等同于urllib 获取url链接的html文件
import xlwt
import sqlite3

# 建立保存路径
savepath = ".\\src\\ExcelFile\\cskaoyan_ECUN.xls"
dbpath = ".\\src\\Database\\cskaoyan.db"


# 报考年份
findYear = re.compile(r'<dt>考研年份</dt><dd>(\d{4})</dd>', re.S)     # 创建正则表达式对象，生成一种字符串模式的特征（表达规则）
                                # (.*?)中间有0个或者多个字符串的情况出现1次或0次
# 报考院校
findTar = re.compile(r'<dt>报考学校</dt><dd>(.*?)</dd>', re.S) # re.S 对所有字符，包括换行符都进行匹配
# 本科院校
findInit = re.compile(r'<dt>本科学校</dt><dd>(.*?)</dd>', re.S)
# 最后登录
findLogin = re.compile(r'<dt>最后登录</dt><dd>(.*?)</dd>', re.S)


# 1. 获取网页端的数据
def getData():

    req = ["http://www.cskaoyan.com/thread-206952-", "-1.html"]
    datalist = []
    spc = "none"

    # 逐条解析数据
    for i in range(126, 140):          # 按页爬取
        tmpurl = req[0] + str(i) + req[1]
        html = askURL(tmpurl)       # 保存获取到的网页源码
        # 逐一解析页面
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('dl', class_="pil cl"):     # 查找符合要求的字符串，形成列表List  此处使用的是BS内部的查找方法
            # 要注意加下划线_      标签名   attri
            # print(item)
            data = []           # 保存一部电影的所需要的信息
            item = str(item)    # 转换成string字符串，使用正则表达式（一群具有某种特征的字符串的集合）查找制定的字符串

            if len(item) == 24:
                continue

            yr = re.findall(findYear, item)    # [0]表示只保存找到的第一个
            if len(yr) != 0:
                data.append(yr)
                # print(yr)
            else:
                data.append(spc)
                # print(spc)

            uniTar = re.findall(findTar, item)
            if len(uniTar) != 0:
                data.append(uniTar)
                # print(uniTar)
            else:
                data.append(spc)
                # print(spc)

            uniInit = re.findall(findInit, item)        # 有中文名和英文名
            if len(uniInit) != 0:
                data.append(uniInit)
                # print(uniInit)
            else:
                data.append(spc)
                # print(spc)

            lastLogin = re.findall(findLogin, item)
            if len(lastLogin) != 0:
                # print(lastLogin)
                data.append(lastLogin[0])
            else:
                data.append(spc)
                # print(spc)

            datalist.append(data)
    # print(datalist)
    return datalist


# SPEC::获取指定URL的网页数据
def askURL(url):
    head = {}
    head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    # 用户代理用来掩盖爬虫Python  告诉服务器本机可以接收什么水平的信息

    request = urllib.request.Request(url, headers=head)

    html = ""
    try:
        res = urllib.request.urlopen(request)
        html = res.read().decode("gbk")
    except  urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 2. 保存数据
def saveData2xsl(datalist, savepath):
    book = xlwt.Workbook(encoding="gbk")
    sheet = book.add_sheet('cskaoyan_ECNU', cell_overwrite_ok=True)
    col = ('报考年份', '报考院校', '本科院校', '最后登录')
    for i in range(0, 4):
        sheet.write(0, i, col[i])  # (x坐标，y坐标，内容)表头  坐标从(0,0)开始
    lenD = len(datalist)
    for i in range(0, lenD):
        data = datalist[i]
        logTime = data[3]
        time_base = '2021-1-1'
        if logTime != 'none' and logTime >= time_base:
            for j in range(0, 4):
                sheet.write(i+1, j, data[j])
            print("第%d条输入" % (i+1))

    book.save(savepath)
    print("Data Saved")


# def init_DB(dbpath):
#     drp_tb = "DROP TABLE TOP250"
#     ck_sql = '''
#         SELECT count(*) FROM sqlite_master WHERE type="table" AND name="TOP250"
#     '''        # 清空数据表
#     sql = '''
#         create table if not exists TOP250
#         (
#         id integer primary key autoincrement,
#         info_link text,
#         fig_link text,
#         chn_name varchar,
#         frn_name varchar,
#         score numeric,
#         rated numeric,
#         instruction text,
#         info text
#         )
#     '''  # 创建数据表
#     conn = sqlite3.connect(dbpath)

#     csr = conn.cursor()

#     cnt = csr.execute(ck_sql)
#     if cnt == 1:
#         csr.execute(sql)
#         print("database initiated")
#         conn.commit()
#         conn.close()
#     else:
#         print("database already exists")
#         choose = input("need overwrite?(Y/N)")
#         if choose == 'Y' or choose == 'y':
#             csr.execute(drp_tb)
#             csr.execute(sql)
#             print("database initiated")
#             conn.commit()
#             conn.close()
#         else:
#             print("RTB")
#             return


# def saveData2DB(datalist, dbpath):
#     init_DB(dbpath)

#     conn = sqlite3.connect(dbpath)
#     cur = conn.cursor()

#     for data in datalist:
#         for index in range(len(data)):
#             if index == 4 or index ==5:
#                 continue
#             data[index] = '"' + data[index] + '"'    # 将数据加上双引号进行输入
#         sql = '''
#             insert into TOP250
#             (info_link,fig_link,chn_name,frn_name,score,rated,instruction,info)
#             values(%s)
#         ''' % ",".join(data)    # 每拼好一行sql进行一次写入
#         cur.execute(sql)
#         conn.commit()
#     cur.close()
#     conn.close()
#     print("DB initiated and saved")


def main():
    datalist = getData()

    # 2. 保存数据
    saveData2xsl(datalist, savepath)


if __name__ == "__main__":
    main()
    # init_DB(dbpath)
