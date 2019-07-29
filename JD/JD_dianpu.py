# -*- coding:utf-8 -*-
import requests
import re
import random
import time
import jsonpath
import openpyxl
import json

'''import pymysql
from sqlalchemy import create_engine
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告'''


# 五折信息的页面  以v2?开头
# 精简请求https://cd.jd.com/promotion/v2?callback=jQuery7173151&skuId=100000540912&area=13_1000_40489_40616&shopId=1000001402&cat=737%2C13297%2C13882


class jd(object):
    def __init__(self):

        self.s = requests.session()  ## 创建一个session对象
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        }


    def getdata(self, url, name):

        getdate = time.strftime("%Y-%m-%d", time.localtime())
        self.shopid = re.search('index-(.*?).html', url).group(1)  ###获取店铺ID号
        self.s.get('https://shop.m.jd.com/search/search?shopId=' + str(self.shopid))

        for i in range(1, 2):  ###爬取页数范围   没有找到商品后会自动退出循环
            wareId_list = []
            wname_list = []
            jdPrice_list = []
            time.sleep(random.random())  ##随机延时0-1秒
            t = int(time.time() * 1000)
            ##           https://wqsou.jd.com/search/searchjson?datatype=1&page=2&pagesize=40&merge_sku=yes&qp_disable=yes&key=ids%2C%2C121614&_=1537524375713&sceneval=2&g_login_type=1&callback=jsonpCBKQ&g_ty=ls
            searchurl = 'https://wqsou.jd.com/search/searchjson?datatype=1&page={}&pagesize=40&merge_sku=yes&qp_disable=yes&key=ids%2C%2C{}&_={}&sceneval=2&g_login_type=1&callback=jsonpCBKA&g_ty=ls'.format(i, self.shopid, t)  ##请求数据网址
            print(searchurl)

            req = self.s.get(url=searchurl, verify=False) ###获取数据



            res = jsonpath.jsonpath(req, '$..jsonpCBKA')
            print(type(res))
            print(res)





            #data = json.loads(req)
            #print(data)
            #wareid = jsonpath.jsonpath(e,'$..Content')
            #print(wareid)








if __name__ == '__main__':
    j = jd()
    url = 'https://mall.jd.com/index-1000001402.html'
    nm = 'intel'
    data = j.getdata(url, nm)

