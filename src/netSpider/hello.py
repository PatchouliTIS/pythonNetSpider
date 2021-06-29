from bs4 import BeautifulSoup      # 网页解析，获取数据
import urllib.request   # 制定url获取网页数据
import urllib.error

import requests

import re       # 正则表达式，文字匹配
import xlwt     # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

# 3. 保存数据（excel  SQLite）
savepath = ".\\doubanTop250films.xls"


def getData(url):
    try:
        # 1. requests库的使用
        r = requests.get(url, timeout=30)
        r.raise_for_status()    # 返回对象的状态码status不是200 就抛出访问异常
        r.encoding = r.apparent_encoding        # 记得改成显式的编码方式apparent_encoding
        return r.text
    except:
        return "连接异常"


# requests库是基于HTTP协议（TCP\IP）来进行数据访问的
def requestData(url):
    try:
        # 查询GET 将字典添加到查询参数**kwargs 也就是param参数，用于向服务器提交限定查询（可选）
        kV = {"key1": "val1", "key2": "val2"}   # dict
        r = requests.request('GET', url, params=kV) # params可以是字典、字节序列或者文件对象

if __name__ == '__main__':
    url = "https://www.baidu.com/"
    print(getData(url))
