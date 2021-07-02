from bs4 import BeautifulSoup
import  re
import requests


# 1. ��ȡ��ҳ�˵�����
def getHMTL_Text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""       # ֱ�ӷ��ؿ��ַ���ֵ


# 2. ��ȡ��ҳ����Ϣ���洢�����ʵ����ݽṹ��
def fillUNI_LIST(ulist, hmtl):
    soup = BeautifulSoup(hmtl, "html.parser")
    
    pass


# 3. �����ݽṹ��װ��չʾ���
def printINFO(ulist, num):
    print("Suc" + str(num))


def main():
    uinfo = []
    tar_url = "https://www.shanghairanking.cn/rankings/bcur/2021"
    tar_html = getHMTL_Text(tar_url)
    fillUNI_LIST(uinfo, tar_html)
    printINFO(uinfo, 20)    # ֻ��ӡǰ20��


main()
