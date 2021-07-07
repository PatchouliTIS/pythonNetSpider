from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import requests


# 1. ��ȡ��ҳ�˵�����
def getData(url):
    datalist = []

    # ������������
    for i in range(0, 10):          # ���û�ȡҳ��ĺ���10�Σ�һҳ25����¼
        tmpurl = url + str(i*25)
        html = askURL(tmpurl)       # �����ȡ������ҳԴ��
        # ��һ����ҳ��

    return datalist

# SPEC::��ȡָ��URL����ҳ����
def askURL(url):
    head = {}
    head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    # �û����������ڸ�����Python  ���߷������������Խ���ʲôˮƽ����Ϣ

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

# 2. ��������
def saveData(savepath):
    print("data saved")


def main():
    baseurl = "https://movie.douban.com/top250?start="
    askURL(baseurl)
    # 1. ��ȡ����
    # datalist = getData(baseurl)

    # 2. ��������·��
    # savepath = ".\\TOP250films.xls"

    # 3. ��������
    # saveData(savepath)

if __name__ == "__main__":
    main()
