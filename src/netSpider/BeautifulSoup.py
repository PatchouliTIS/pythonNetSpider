from ssl import enum_certificates
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
# BS4是用来解析html和xml文档的功能库  信息标记类型文本解析器
# 返还一个beautiful soup类树形对象，是将html文本中的标签形成标签树，方便针对标签或者标签类型、所含字段进行查找遍历的一种工具
# bs树形结构对象包含的成员：Tag(~.<tag名字>), NavigableString(~.string 标签的内容), Attribution(~.attrs 属性的键值对，以字典形式返还)
url = "https://movie.douban.com/top250?start="

def getWEB(baseurl):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    req = urllib.request.Request(url=baseurl, headers=head)

    html = ""

    try:
        ret = urllib.request.urlopen(req)
        html = ret.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


#                                  解析方式：html
soup = BeautifulSoup(getWEB(url), "html.parser")
# 也可以通过打开文件的方式新建一个BS库
# soup = BeautifulSoup(open("D://balabala.html", "html.parser"))

# print(soup.title) <title>...</title>标签


# 用~.prettify()方法来实现对人友好的显示界面
print(soup.a.prettify())
print(type(soup.a))
# 注意：bs4库自动使用UTF-8编码，和PY3.X兼容