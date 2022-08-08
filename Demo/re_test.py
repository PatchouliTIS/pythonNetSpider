# -*- coding: utf-8 -*-
# re_test.py
# @author Patchouli Tisa
# @description RLTW
# @created 2021-07-10T16:40:15.820Z+08:00
# @last-modified 2021-09-14T11:38:53.378Z+08:00
#

import re
import urllib
import urllib.request
from bs4 import BeautifulSoup

findlink = re.compile(r'<a href="(.*?)">')
findIMG_L = re.compile(r'src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')

datalist = []


def getHTML(baseurl):
    html = ""
    head = {}
    head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    try:
        request = urllib.request.Request(baseurl, headers=head)
        resp = urllib.request.urlopen(request)
        html = resp.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getDATA(html):
    datalist = []
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="item"):
        data = []
        # 将BS标签树类对象item转换为字符串，以供re查询使用
        item = str(item)

        link = re.findall(findlink, item)[0]
        data.append(link)

        Img_src = re.findall(findIMG_L, item)
        # print(Img_src)
        # print(len(Img_src))
        data.append(Img_src)

        title = re.findall(findTitle, item)
        if len(title) < 2:
            data.append(title[0])
            data.append("")
        else:
            data.append(title[0])
            aft = title[1]      # .replace("/", "")
            data.append(aft)

        datalist.append(data)

    return datalist


def main():
    bvs = "https://movie.douban.com/top250?start="
    html = getHTML(bvs)
    datalist = getDATA(html)
    for item in datalist:
        print("%s" % ",".join(item))


if __name__ == '__main__':
    main()
