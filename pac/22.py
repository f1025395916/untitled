import requests

url="http://www.baidu.com/s?"

kw = {

    "wd" :"王八蛋"
}

headers = {

    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
rsp = requests.get(url,params=kw,headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.headers)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code) # 请求返回码