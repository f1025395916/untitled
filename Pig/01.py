'''
 http://zdscxx.moa.gov.cn:8080/misportal/public/agricultureMessageViewDC.jsp
 爬取农村农业部列表，生猪存栏信息
'''
import requests
from lxml import etree

# 返回的json存放
result_list = []
# 发布时间存放
time_list = []
# 标题存放
title_list =[]
# 链接存放
link_list =[]



for i  in range(1,57):
    # 接口连接
    url = "http://zdscxx.moa.gov.cn:8080/misportal/echartReport/webData/%E6%9C%80%E6%96%B0%E5%8F%91%E5%B8%83/page{}.json?_=1566886444158".format(str(i))


    # 发送请求，获取响应
    response = requests.get(url)
    requests_dict = response.json()

    for data in requests_dict:
        if  data["realChannel"]=="生猪存栏":
            result_list.append(dict(data))



print(result_list)
print(len(result_list))

for i in result_list:
    print("时间：{}".format(i["publishTime"]))
    print("标题：{}".format(i["title"]))
    print("链接：{}".format(i["link"]))

    # 解析网页
    htmlEmt = etree.parse(i["link"],etree.HTMLParser())
    # 比上月增减  生

    lastMoth_youth_list = htmlEmt.xpath('//tbody/tr[2]/td[2]/p/span/text()')
    print("生存栏比上个月增减{}".format(lastMoth_youth_list))

    # 比上月增减  母
    lastMoth_female_list= htmlEmt.xpath("//tbody/tr[2]/td[3]/p/span/text()")
    print("母存栏比上个月增减{}".format(lastMoth_female_list))

    # 比去年同期增减  生
    lastYear_youth_list = htmlEmt.xpath("//tbody/tr[3]/td[2]/p/span/text()")
    print("生存栏比去年同期增减{}".format(lastYear_youth_list))

    # 比去年同期增减  母
    lastYear_female_list = htmlEmt.xpath("//tbody/tr[3]/td[3]/p/span/text()")
    print("母存栏比去年同期增减{}".format(lastYear_female_list))








