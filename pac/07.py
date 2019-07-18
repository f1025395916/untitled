from urllib import  request,error

if __name__=="__main__":
    url = "http://www.baiiiiiiiiiiiidu.com"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e :
        print("UrlError:{0}".format(e.reason))
        print("UrlError:{0}".format(e))
    except Exception as e :
        print(e)