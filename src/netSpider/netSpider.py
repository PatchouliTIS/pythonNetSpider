from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
# import requests   作用等同于urllib 获取url链接的html文件
import xlwt
import sqlite3

# 建立保存路径
savepath = ".\\src\\netSpider\\TOP250films.xls"
dbpath = ".\\src\\netSpider\\filmsDataBase.db"


# findLink方法  获取影片详情链接的字符串规则
findLink = re.compile(r'<a href="(.*?)">')     # 创建正则表达式对象，生成一种字符串模式的特征（表达规则）
                                # (.*?)中间有0个或者多个字符串的情况出现1次或0次
# 得到图片源
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S) # re.S 对所有字符，包括换行符都进行匹配
# 得到片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
# 得到评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 得到评价人数
findRecomm = re.compile(r'<span>(\d*)人评价</span>')
# 得到介绍
findInfo =re.compile(r'<span class="inq">(.*)</span>')
# 得到内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

# 1. 获取网页端的数据
def getData(url):
    datalist = []

    # 逐条解析数据
    for i in range(0, 10):          # 调用获取页面的函数10次，一页25条记录
        tmpurl = url + str(i*25)
        html = askURL(tmpurl)       # 保存获取到的网页源码

        # 逐一解析页面
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):     # 查找符合要求的字符串，形成列表List  此处使用的是BS内部的查找方法
            # 要注意加下划线_      标签名   attri
            # print(item)
            data = []           # 保存一部电影的所需要的信息
            item = str(item)    # 转换成string字符串，使用正则表达式（一群具有某种特征的字符串的集合）查找制定的字符串
            link = re.findall(findLink, item)[0]    # [0]表示只保存找到的第一个
            data.append(link)
            # print(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)        # 有中文名和英文名
            if len(titles) == 2:
                chnTitle = titles[0]
                data.append(chnTitle)
                frnTitle = titles[1].replace("/", "")   # 去掉斜杠
                data.append(frnTitle)
            else:
                data.append(titles[0])
                data.append(" ")        # 没有外文名则留空，为之后的制表做准备

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            recomm = re.findall(findRecomm, item)[0]
            data.append(recomm)

            info = re.findall(findInfo, item)    # 不写[0]
            if len(info) == 0 :
                data.append(" ")
            else:
                info = info[0].replace("。", "")
                data.append(info)

            Bd = re.findall(findBd, item)[0]
            Bd = re.sub('<br(\s+)?/>(\s+)?', " ", Bd)  # 去掉<br/>
            Bd = re.sub('/', " ", Bd)   # 去掉/
            data.append(Bd.strip())     # 去掉前后空格

            datalist.append(data)

    # print(datalist)
    return datalist


# SPEC::获取指定URL的网页数据
def askURL(url):
    head = {}
    head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    # 用户代理用来掩盖爬虫Python  告诉服务器本机可以接收什么水平的信息

    request = urllib.request.Request(url, headers=head)

    html = ""
    try:
        res = urllib.request.urlopen(request)
        html = res.read().decode("utf-8")
    except  urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 2. 保存数据
def saveData2xsl(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('TOP250films', cell_overwrite_ok=True)
    col = ('电影链接', '图片链接', '影片中文名', '影片外文名', '评分', '评价人数', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 表头
    for i in range(0, 250):
        data = datalist[i]

        for j in range(0, 8):
            sheet.write(i+1, j, data[j])
        print("第%d条输入" % (i+1))

    book.save(savepath)
    print("Data Saved")


def init_DB(dbpath):
    drp_tb = "DROP TABLE TOP250"
    ck_sql = '''
        SELECT count(*) FROM sqlite_master WHERE type="table" AND name="TOP250"
    '''        # 清空数据表
    sql = '''
        create table if not exists TOP250
        (
        id integer primary key autoincrement,
        info_link text,
        fig_link text,
        chn_name varchar,
        frn_name varchar,
        score numeric,
        rated numeric,
        instruction text,
        info text
        )
    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)

    csr = conn.cursor()

    cnt = csr.execute(ck_sql)
    if cnt == 1:
        csr.execute(sql)
        print("database initiated")
        conn.commit()
        conn.close()
    else:
        print("database already exists")
        choose = input("need overwrite?(Y/N)")
        if choose == 'Y' or choose == 'y':
            csr.execute(drp_tb)
            csr.execute(sql)
            print("database initiated")
            conn.commit()
            conn.close()
        else:
            print("RTB")
            return


def saveData2DB(datalist, dbpath):
    init_DB(dbpath)

    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index ==5:
                continue
            data[index] = '"' + data[index] + '"'    # 将数据加上双引号进行输入
        sql = '''
            insert into TOP250
            (info_link,fig_link,chn_name,frn_name,score,rated,instruction,info)
            values(%s)
        ''' % ",".join(data)    # 每拼好一行sql进行一次写入
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print("DB initiated and saved")


def main():
    baseurl = "https://movie.douban.com/top250?start="
    askURL(baseurl)
    # 1. 获取数据
    datalist = getData(baseurl)
    # 2. 保存数据
    # saveData2xls(datalist, savepath)
    saveData2DB(datalist, dbpath)

if __name__ == "__main__":
    main()
    # init_DB(dbpath)
