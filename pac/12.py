from urllib import request,error

if __name__=="__main__":
    url = "http://www.renren.com/971289729/profile"
    headers = {
        'Cookie':'anonymid=jxbgvoeexv5jvm; depovince=SD; _r01_=1; JSESSIONID=abcMKxyXWtVbB7cHxDnUw; ick_login=956b7790-4b6b-4f42-b4f8-f0a03c4a1980; t=2ff5e28236572adec229139b463dddb79; societyguester=2ff5e28236572adec229139b463dddb79; id=971289729; xnsid=728a6bdf; jebecookies=ffa4faf8-b35a-4a1e-bbc3-b5e8428c4da4|||||; ver=7.0; loginfrom=null; jebe_key=3a6a73df-4e70-4f28-9b3a-efb863c06d8a%7C7c832b9b054c382c61cf1a70c3aa9e2c%7C1561446423081%7C1%7C1561446422271; jebe_key=3a6a73df-4e70-4f28-9b3a-efb863c06d8a%7C7c832b9b054c382c61cf1a70c3aa9e2c%7C1561446423081%7C1%7C1561446422274; wp_fold=0; wp=0'

    }
    req = request.Request(url,headers=headers)
    rsp =request.urlopen(req)
    html = rsp.read().decode()

    with open("rsp.html","w",encoding='utf-8') as f:
        f.write(html)
