from urllib import  request,error

if __name__=='__main__':
    url ="http://www.baidu.com"
try:
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    req  = request.Request(url,headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print(e)
except error as e:
    print(e)
