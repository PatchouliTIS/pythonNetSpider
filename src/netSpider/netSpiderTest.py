import requests


def getNetData(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return [r.status_code, r.encoding, r.headers]
    except:
        return "异常"


url = "https://item.jd.com/35875527661.html"

arr = getNetData(url)

for text in arr:
    print(text)
