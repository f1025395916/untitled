# -*- coding: gb2312 -*-
from urllib import  request,parse
from http import cookiejar

# ����filecookiejar��ʵ��

cookie =cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)


# ����cookie�Ĺ�����
cookie_handle = request.HTTPCookieProcessor(cookie)

# ����http���������
http_handle = request.HTTPHandler()

# ����https������
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

    # ���浽cookie�ļ�
    # ignor_discard ��ʾ��ʱcookie��Ҫ������ҲҪ��������
    # ignor_expire ��ʾ������ļ���cookie��������ҲҪ����
    cookie.sava(ignore_discard=True,ignore_expire=True)


if __name__=="main":
    login()
