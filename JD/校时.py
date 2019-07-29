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

print(r.json())





res = jsonpath.jsonpath(r.json(),'$..serverTime')
print(str(res))







timeTemp = str(res[0])
# 最后三位的毫秒数    288
lMillisecond = str(timeTemp)[10:16]

# 获取秒的时间戳    1563443717288
second = str(timeTemp)[0:10]

# 转换为元祖
timeArray = time.localtime(int(second))

# 转换后的时间 2019--07--18
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)


print('获取前三位的毫秒数：{}'.format(str(timeTemp)[10:13]))

time3 = str(timeTemp)[10:13]

time_now = datetime.datetime.now().strftime('%H:%M:%S.%f')
print('当前时间：{0}'.format(time_now))
# 转换后的时间和毫秒结合  2019--07--18 17:55:17.288
otherStyleTime = otherStyleTime + '.' + lMillisecond
print("服务器时间：{}".format(otherStyleTime))

time_now = datetime.datetime.now().strftime('%H:%M:%S.%f')
print('当前时间：{0}'.format(time_now))








_date =time.strftime("%Y/%m/%d",timeArray)
_time =time.strftime("%X",timeArray)
#threeTime = str(timeTemp)[10:12]
#_time +='.{}'.format(threeTime)
print(_date)
print(_time)

waitTime =   (1000 - int(time3))/1000

print(waitTime)
time.sleep(waitTime)

os.system('date {}'.format(_date))
os.system('time {}'.format(_time))






# 设置时间需要4毫秒19:55:50.004000
time_end = datetime.datetime.now().strftime('%Y--%m--%d  %H:%M:%S.%f')
print("程序结束时间：{}".format(time_end))






