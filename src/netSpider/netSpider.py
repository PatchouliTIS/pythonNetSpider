from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import requests


# 1. 获取网页端的数据
def getData(url):
    datalist = []

    # 逐条解析数据
    for i in range(0, 10):          # 调用获取页面的函数10次，一页25条记录
        tmpurl = url + str(i*25)
        html = askURL(tmpurl)       # 保存获取到的网页源码
        # 逐一解析页面

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
def saveData(savepath):
    print("data saved")


def main():
    baseurl = "https://movie.douban.com/top250?start="
    askURL(baseurl)
    # 1. 获取数据
    # datalist = getData(baseurl)

    # 2. 建立保存路径
    # savepath = ".\\TOP250films.xls"

    # 3. 保存数据
    # saveData(savepath)

if __name__ == "__main__":
    main()
