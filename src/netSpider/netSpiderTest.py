from bs4 import BeautifulSoup
import requests
import re
# BS4是用来解析html和xml文档的功能库  信息标记类型文本解析器
#
def getText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return "读取异常"


def getNetData(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return [r.status_code, r.encoding, r.headers, r.text]
    except:
        return "异常"


url = "https://www.icourse163.org/learn/BIT-1001870001"

arr = getNetData(url)

for text in arr:
    print(text)

#                              解析方式：html
target_text = getText(url)
soup = BeautifulSoup(target_text, "html.parser")
# 也可以通过打开文件的方式新建一个BS库
# soup = BeautifulSoup(open("D://balabala.html", "html.parser"))

# print(soup.title)
# 用~.prettify()方法来实现对人友好的显示界面
print(soup.prettify())
# 注意：bs4库自动使用UTF-8编码，和PY3.X兼容