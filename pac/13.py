# coding=gbk
from urllib import request,error,parse
from http import cookiejar

cookie = cookiejar.CookieJar()
#����cookie������
cookie_handle = request.HTTPCookieProcessor(cookie)
#����http������
http_handle = request.HTTPHandler()
#����https������
https_handle = request.HTTPSHandler()
# �������������
opener = request.build_opener(http_handle,https_handle,cookie_handle)


def login():
    url="http://www.renren.com/PLogin.do"
    data = {
        "email":"18660653953",
        "password":"fs54264546"
    }
    # �����ݽ��б���
    data=parse.urlencode(data)
    # ����һ���������
    req = request.Request(url,data=data.encode())
    # ʹ��opener����
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

