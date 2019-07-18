# coding=gbk
from urllib import request,error,parse
from http import cookiejar

cookie = cookiejar.CookieJar()
#生成cookie管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
#生成http管理器
http_handle = request.HTTPHandler()
#生成https管理器
https_handle = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handle,https_handle,cookie_handle)


def login():
    url="http://www.renren.com/PLogin.do"
    data = {
        "email":"18660653953",
        "password":"fs54264546"
    }
    # 把数据进行编码
    data=parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url,data=data.encode())
    # 使用opener发起
    rep = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/860949455/profile"
    rsp = opener.open(url)
    html =rsp.read().decode()
    with open("rsp.html","w",encoding='utf-8') as f:
        f.write(html)

if __name__=='__main__':
    login()
    getHomePage()

