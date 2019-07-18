from urllib import  request,parse
import json

baseurl="https://fanyi.baidu.com/sug"
# 存放模拟form的数据一定是dict格式
data ={
    'kw':'girl'
}
# 需要使用parse对data进行编码
data = parse.urlencode(data).encode()

# 我们需要构造一个请求头
headers = {
    #因为使用post,至少应该包含content-length字段
    'Content-Length':len(data)
}
# 有了headers,data,url就可以发送请求了
rsp = request.urlopen(baseurl,data=data)
json_data = rsp.read().decode("utf-8")
print(type(json_data))
print(json_data)

# 把json字符串转换成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data["data"]:
    print(item)