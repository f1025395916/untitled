from urllib import  request


if __name__ =="__main__":
    url ='https://jobs.zhaopin.com/CC875695080J00143090814.htm'
    rsp = request.urlopen(url)
    # 把返回结果输出
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))
    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode("utf-8")
    print(html)


