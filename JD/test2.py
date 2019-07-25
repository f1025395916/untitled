import time

timeTemp ='1563443717288'
# 最后三位的毫秒数    288
lMillisecond = str(timeTemp)[10:13]

# 获取秒的时间戳    1563443717288
second = str(timeTemp)[0:10]

# 转换为元祖
timeArray = time.localtime(int(second))

# 转换后的时间 2019--07--18
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)

# 转换后的时间和毫秒结合  2019--07--18 17:55:17.288
otherStyleTime = otherStyleTime + '.' + lMillisecond
print(otherStyleTime)
