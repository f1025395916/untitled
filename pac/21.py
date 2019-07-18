# -*- coding:gbk -*-
import  requests


url="http://www.baidu.com"
# 两种请求方式
rsp =requests.get(url)
print(rsp.text)

rsp2 = requests.request("get",url)
print(rsp2.text)