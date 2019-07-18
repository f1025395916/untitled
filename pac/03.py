import urllib
import chardet
import requests
if __name__=="__main__":
    url="http://stock.eastmoney.com/a/201906241159242286.html"
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)
    print("url:{0}".format(rsp.geturl()))
    print("info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

