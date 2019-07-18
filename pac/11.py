from urllib import request,error

if __name__=="__main__":
    url ="http://www.renren.com/971289729/profile"
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)


    with open("rsp.html","w",encoding='utf-8') as f:
        f.write(html)
