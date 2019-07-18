import  datetime
import ntplib
import os
import time
import json
import urllib.request
import guid
import jsonpath


'''
c = ntplib.NTPClient()
response = c.request('pool.ntp.org')
ts = response.tx_time

_date = time.strftime('%Y-%m-%d',time.localtime(ts))
_time = time.strftime('%H:%M:%S',time.localtime(ts))
print(_date)
print(_time)
print(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S:%f]"))
'''
url = "https://a.jd.com//ajax/queryServerData.html"

req = urllib.request.Request(url)

req.add_header("UserAgent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
data = urllib.request.urlopen(req).read().decode("utf-8")
data = json.loads(data)
jsondate = jsonpath.jsonpath(data,"$.serverTime")
print(jsondate)
timeStamp = jsondate[0]

print(timeStamp)
sortTime =str(timeStamp)[0:10]
lMillisecond = str(timeStamp)[10:13]
print(lMillisecond)
print(sortTime)
timeArray = time.localtime(int(sortTime))
otherStyleTime  = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
otherStyleTime = otherStyleTime +'.'+lMillisecond
print(otherStyleTime)










