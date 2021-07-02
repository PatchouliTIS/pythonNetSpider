from bs4 import BeautifulSoup
import  re
import requests


# 1. 获取网页端的内容
def getHMTL_Text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""       # 直接返回空字符串值


# 2. 提取网页端信息并存储到合适的数据结构中
def fillUNI_LIST(ulist, hmtl):
    soup = BeautifulSoup(hmtl, "html.parser")
    
    pass


# 3. 用数据结构封装并展示结果
def printINFO(ulist, num):
    print("Suc" + str(num))


def main():
    uinfo = []
    tar_url = "https://www.shanghairanking.cn/rankings/bcur/2021"
    tar_html = getHMTL_Text(tar_url)
    fillUNI_LIST(uinfo, tar_html)
    printINFO(uinfo, 20)    # 只打印前20名


main()
