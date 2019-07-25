import os
import time
import requests
import json
import jsonpath
import datetime


url = "https://a.jd.com//ajax/queryServerData.html"

headers ={

            'Method':'get',
            'UserAgent ':'PC_USER_GENT'
}
r = requests.post(url,headers=headers)
#在发送请求和响应到达之前耗费的时间差（timedelta），指发送第一个byte数据头至处更完最后一个数据头之间，所以这个时长不受相应的内容影响。
print(r.elapsed.microseconds)
print("请求延迟毫秒数：{}".format(r.elapsed))

res = jsonpath.jsonpath(r.json(),'$..serverTime')
print(str(res))

timeTemp = str(res[0])
# 最后三位的毫秒数    288
lMillisecond = str(timeTemp)[10:13]

# 获取秒的时间戳    1563443717288
second = str(timeTemp)[0:10]

# 转换为元祖
timeArray = time.localtime(int(second))

# 转换后的时间 2019--07--24 09:31:24
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)

# 服务器时间：2019--07--24 09:31:24.878
otherStyleTime = otherStyleTime + '.' + lMillisecond
print("服务器时间：{}".format(otherStyleTime))


_date =time.strftime("%Y/%m/%d",timeArray)
_timeStr =time.strftime("%H:%M:%S",timeArray)

_time = datetime.datetime.strptime(_timeStr,"%H:%M:%S")
print(_time)
#  时间多加一秒
time1 = (_time+datetime.timedelta(seconds=1)).strftime("%H:%M:%S")
print(time1)

# 要等待的时间秒

waitTime =(1000 - int(lMillisecond))/1000
time.sleep(waitTime)
print(waitTime)

# 修改系统时间
os.system('date {}'.format(_date))
os.system('time {}'.format(time1))


time_end = datetime.datetime.now().strftime('%Y--%m--%d  %H:%M:%S.%f')
print("程序结束时间：{}".format(time_end))