import requests
import json
import time
import pdfkit

def get_content_url(index,biz,uin,key):
    #print("*"*20)
    #print("正在爬取第{}页".format(index+1))

    # url 前缀
    url= "https://mp.weixin.qq.com/mp/profile_ext"

    # 请求头
    headers ={

        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/3.53.1159.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat',
        'Cookie':'rewardsn =;    wxtokenkey = 777;    wxuin = 2966837921;    devicetype = WindowsServer2008R2;    version = 62060833;    lang = zh_CN;    pass_ticket = 52    UDxbm + PkSfazCn2HE9Gny1M + 3    FEhWZx3AViTzV + sCwbVECcl + Pqh / kcCOTshjM;    wap_sid2 = CKG12YYLElxmVkZiZkdpWEdJY3hYM2ZWSGlIVGloMXZlUHRfdmxzdXo5UnRGRWw0NEdqc3BnUlpaajJsZ0MwTm8tR0N4ck1RSUl1RUk3YlhRUzZtWHNDMzNWYmxEdjhEQUFBfjDDifnqBTgNQJVO ',
        'Host':'mp.weixin.qq.com',
        'Referer':'https://mp.weixin.qq.com/mp/profile_ext'

           }
    if index!=0:
        index = index*10+1
    # 重要参数
    param = {
        'action':'getmsg',
        '__biz':biz,
        'f':'json',
        'offset':index,
        'uin':uin,
        'key':key



    }

    # 发去请求，获取相应
    response  = requests.get(url,params=param,headers=headers)
    response_dict = response.json()

    #print(response_dict)

    next_offset =response_dict["next_offset"]

    can_msg_continue =response_dict["can_msg_continue"]
    general_ms_list = response_dict["general_msg_list"]
    data_list = json.loads(general_ms_list)["list"]

    #print(data_list)

    for data in data_list:
        try:
            datetime = data['comm_msg_info']['datetime']
            date = time.strftime('%Y-%m-%d',time.localtime(datetime))

            msg_info = data['app_msg_ext_info']
            # 标题
            title = msg_info['title']
            # 内容的url
            content_url = msg_info['content_url']

            print(title + date +'---' +content_url)

            # 自己定义存储路径（绝对路径）
            #pdfkit.from_url(content_url,'F:/公众号文章/远方青木/'+date+title+'.pdf')

            #print(title+date+'成功')
            print('*'*20)
        except:
            print("不是图文消息")
    if can_msg_continue==1:
        return True
    else:
        print("全部获取完毕")
        return False

#GET /mp/profile_ext?action=getmsg&__biz=&f=json&offset=91&count=10&is_ok=1&scene=124&uin=Mjk2NjgzNzkyMQ%3D%3D&key=&pass_ticket=52UDxbm%2BPkSfazCn2HE9Gny1M%2B3FEhWZx3AViTzV%2BsCwbVECcl%2BPqh%2FkcCOTshjM&wxtoken=&appmsg_token=1023_qkwxoGC9Sf%252FE3I%252B6QAIAvHnZWT7LDKDdoROYSw~~&x5=0&f=json HTTP/1.1



if __name__ == '__main__':

    index = 0

    # 这三个参数要换成自己的

    biz = 'MzU5MzcyMzc2OQ=='
    uin = 'Mjk2NjgzNzkyMQ=='
    key = 'c5d73e65710b7a3399b2e3892586f9b74d5c17f21cf8ec23c35f7b7a71aa572dd6a0fa8b419b89dba84bdb7a78b8b4cd8aa571a5f5a7239486c047d2c6ae9387adfb82c0070cb9a3a99eb448e4383922'

    while 1:

        result = get_content_url(index, biz, uin, key)

        time.sleep(2)
        index += 1

        if result == False:
            break




