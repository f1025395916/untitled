# -*- coding: gb2312 -*-
from urllib import  request,parse
from http import cookiejar

# 创建filecookiejar的实例

cookie =cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)


# 创建cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handle = request.HTTPHandler()

# 生成https管理器
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

    # 保存到cookie文件
    # ignor_discard 表示及时cookie将要被抛弃也要保存下来
    # ignor_expire 表示如果该文件中cookie即将过期也要保存
    cookie.sava(ignore_discard=True,ignore_expire=True)


if __name__=="main":
    login()
