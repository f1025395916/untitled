import requests
import json
import time
import pdfkit

def get_content_url(index,biz,uin,key):
    print("*"*20)
    print("正在爬取第{}页".format(index+1))

    # url 前缀
    url= "https://mp.weixin.qq.com/mp/profile_ext"

    # 请求头
    headers ={

        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/3.53.1159.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat',
        'Cookie':'rewardsn=; wxtokenkey=777; wxuin=2966837921; devicetype=WindowsServer2008R2; version=62060833; lang=zh_CN; pass_ticket=oIUeB5o7KFsOTPBintRZtctISUKO8X2WYLP8TSCksGOvvWMev/1wjP7Nr3j0WoFs; wap_sid2=CKG12YYLEnBWN0hLdDVBU0ExRHZpSDBHWDY4WDFyS2Q0T3pwRkdNRHRCWTlaVG92TUUzMUMwcFdFaERDZkVOZjJmbDc1VXV1aVNhLVIwNmxaWFpSbWU2dFFpdUVuSGJ3S0tJN1UxQVhPM1lua0k0ZnhoZjlBd0FBMM+Dr+oFOA1AlU4=',
        'Host':'mp.weixin.qq.com',
        'Referer':'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU5MzcyMzc2OQ==&scene=124&uin=Mjk2NjgzNzkyMQ%3D%3D&key=1db4607b45ac1236e692b2506978d20d3cb7fc2e8fe840ced9415da9be8043d863a55fa62fb1b3664bf6411a55608f6d7ed11f27f93249b6d9388c640ea5ec0afb45de62775f457e06cad0cd4175c0ac&devicetype=Windows+Server+2008+R2&version=62060833&lang=zh_CN&a8scene=7&pass_ticket=oIUeB5o7KFsOTPBintRZtctISUKO8X2WYLP8TSCksGOvvWMev%2F1wjP7Nr3j0WoFs&winzoom=1'


    }

    # 重要参数
    param = {
        'action':'getmsg',
        '__biz':biz,
        'f':'json',
        'offset':index *10,
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

    print(data_list)

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
            pdfkit.from_url(content_url,'F:/公众号文章/远方青木/'+date+title+'.pdf')

            print(title+date+'成功')
            print('*'*20)
        except:
            print("不是图文消息")
    if can_msg_continue==1:
        return True
    else:
        print("全部获取完毕")
        return False





if __name__ == '__main__':

    index = 0

    # 这三个参数要换成自己的

    biz = 'MzU5MzcyMzc2OQ=='
    uin = 'Mjk2NjgzNzkyMQ=='
    key = '1db4607b45ac1236e692b2506978d20d3cb7fc2e8fe840ced9415da9be8043d863a55fa62fb1b3664bf6411a55608f6d7ed11f27f93249b6d9388c640ea5ec0afb45de62775f457e06cad0cd4175c0ac'

    while 1:

        result = get_content_url(index, biz, uin, key)

        time.sleep(2)
        index += 1

        if result == False:
            break




