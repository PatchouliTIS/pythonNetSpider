import urllib
import urllib.request
import urllib.parse      # 解析器，模拟请求报文

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# 在POST方法中，还有一种参数是data，类型是二进制字典dict
# 用于向服务器端提交data内提供的二进制键值对数据
# data = bytes(urllib.parse.urlencode({"name":"YJSP"}), encoding="utf-8")
req = urllib.request.Request(url=url, headers=headers)
request = urllib.request.urlopen(req)
print(request.read().decode("utf-8"))
