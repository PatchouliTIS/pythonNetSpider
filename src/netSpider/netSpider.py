from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import requests


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
            Bd = re.sub('<br(\s+)?/>(\s+)?', " ", Bd) # 去掉<br/>
            Bd = re.sub('/', " ", Bd)   # 去掉/
            data.append(Bd.strip())     # 去掉前后空格

            datalist.append(data)
            
    print(datalist)
    # return datalist

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
def saveData(savepath):
    print("data saved")


def main():
    baseurl = "https://movie.douban.com/top250?start="
    askURL(baseurl)
    # 1. 获取数据
    datalist = getData(baseurl)

    # 2. 建立保存路径
    # savepath = ".\\TOP250films.xls"

    # 3. 保存数据
    # saveData(savepath)

if __name__ == "__main__":
    main()
