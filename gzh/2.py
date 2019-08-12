import requests
import jsonpath

#encodi

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Referer":"https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&lang=zh_CN&token=75428446&token=75428446&lang=zh_CN",
    "Host":"mp.weixin.qq.com",
    "Cookie":"noticeLoginFlag=1; remember_acct=1025395916%40qq.com; pgv_pvi=5841408000; RK=vGNfaYNiW6; ua_id=y8UUVVnDgU2I6TYSAAAAAFMjHOJcRL1xoFIjTtIhOMk=; tvfe_boss_uuid=88b5080437315ac0; pgv_pvid=1599016657; o_cookie=1025395916; ptcz=87d0fcd103c2c5ed993d663a0a74c2ce9e008d644a2cfbce9d9ae202fb047811; eas_sid=X135I3L891p0P959B994z5y525; pac_uid=1_1025395916; LW_uid=c1c5947473i5b2F9x2K8R5A263; mobileUV=1_169e2262b96_a2bca; ied_qq=o1025395916; LW_sid=2165Z6G2i3k1b8Q6P0f4S8J2k6; mm_lang=zh_CN; noticeLoginFlag=1; bizuin=3237528418; pgv_si=s9404317696; uuid=ea32cd5bab995881f817d2aaa21977f2; ticket=1c8b31319dcd11c9eb8ed1d1926f88b13840176d; ticket_id=gh_61af4df1ab2b; cert=nHdwarURj3Xyyx_xYz9NWANwCj5CBhbM; data_bizuin=3237528418; data_ticket=3xJsbFFV+J+tMJvJBuqNN8wta9iCC7K1rERrOD74aihZ/N5M4A2XdGpZVdU+dNDg; slave_sid=akd1dkx3VWpTSVRiWTRXbXJWbUo2R2FDTUs1enpMdmdhemI3NFl1dG1GaWFtekF1a0tJRTFneTA4SENKMlVCMG9uZVdvaDVrRE1pZnc2UVdhWHZybk1FY0NxSU94S095a2kwVGJCUDNDc082OGpkckI4VnVzTWdZVzNnSktTVDFrdVhDZzZHT3JnTnptTDBk; slave_user=gh_61af4df1ab2b; xid=05717b4c07d65b7a6a3c1a1526edb96c; openid2ticket_oYsP4wGTD7oLbKEW6h9TsXbSBk98=lEv9BmrH1oevYQikC9dTGvQDhC3ugowiDIB02Z4HjqE=",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"



}
urlList =[]
titleList =[]
for i in range(37):
    url ="https://mp.weixin.qq.com/cgi-bin/appmsg?token=1939812004&lang=zh_CN&f=json&ajax=1&random=0.8002129730533283&action=list_ex&begin={}&count=5&query=&fakeid=MzU5MzcyMzc2OQ%3D%3D&type=9".format(str(i*5))

    response = requests.get(url,headers=headers)
    jsonRes = response.json()
    print(jsonRes)

    titleList = jsonpath.jsonpath(jsonRes,"$..title")

    urlList = jsonpath.jsonpath(jsonRes,"$..link")

    # 遍历 构造可存储字符串
    while(titleList  is True):
        for index in range(len(titleList)):
            title = titleList[index]
        url = urlList[index]
        '''
        scvStr = "%s,%s,\n" % (title, url)
        with open("info.csv", "a+", encoding="utf-8", newline="")as f:
            f.write(scvStr)
        '''
print(">>>>"*10)
print(urlList[0])
print(">>>>"*10)
print(titleList[0])





