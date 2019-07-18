# 代理
# 1.设置代理地址
# 2.设置ProxyHandle
# 3.创建opener
# 4.安装opener

from urllib import  request,error

if __name__=="__main__":
    url="http://www.baidu.com"
    # 设置代理
    # 1.设置代理地址
    proxy = {'http':'40.73.36.247:3128'}
    # 2.设置ProxyHandle
    proxy_handle = request.ProxyHandler(proxy)
    # 3.创建opener
    opener = request.build_opener(proxy_handle)
    # 4.安装opener
    request.install_opener(opener)
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error as e:
        print(e)

