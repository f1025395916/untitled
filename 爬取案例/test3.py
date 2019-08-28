import urllib.request
import json
import jsonpath
import  requests

url = "http://zhujia.zhuwang.cc/index/api/chartData?areaId=110000&aa=1565837187844"
headers = {

    "cookie":"Hm_lvt_ecf9f117616fbbedc6c0b6847d198f3d=1564017331,1565834356; historyAreaInfo=110000%3B-1; Hm_lpvt_ecf9f117616fbbedc6c0b6847d198f3d=1565837172",
    "Referer":"http://zhujia.zhuwang.cc/areapriceinfo-110000.shtml",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"

}
req = requests.get(url,headers=headers)
data = req.json()
print(data)

