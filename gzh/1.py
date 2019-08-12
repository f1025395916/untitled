import requests

import time
import json
import os



class mp_spider(object):

    def request_data(self):
        try:
            self.base_url ="https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5MTQ4NjA3Nw==&f=json&offset=300&count=10&is_ok=1&scene=124&uin=Mjk2NjgzNzkyMQ%3D%3D&key=7f1669f6bfac5281eecfa3358233b7a3dbef95850c1ff5c6933deeead63f63474c7c20ce1cdd944124f6b40f1a59ea4a2dce438926932d31d987c3e7817b64d9659b49ce0b74f478df5e98c5c7b50d60&pass_ticket=zJSGVkrv4OaAylJdVtyg%2FEKqgQrPP%2B9v4ZHwLL%2FwwwTQNs1HOUkQAjqbl1AbboLq&wxtoken=&appmsg_token=1020_nB%252BV%252FiDQ%252FjOtWc6JK-mGAnKzClRGunRSlsxP0w~~&x5=0&f=json"
            self.offset =""
            self.headers ={
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/3.53.1159.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat",
                "Cookie":"rewardsn=; wxtokenkey=777; wxuin=2966837921; devicetype=WindowsServer2008R2; version=62060833; lang=zh_CN; pass_ticket=zJSGVkrv4OaAylJdVtyg/EKqgQrPP+9v4ZHwLL/wwwTQNs1HOUkQAjqbl1AbboLq; wap_sid2=CKG12YYLElw3bEpuNVNMb19MeEhEb1AxNmF4TU9hMGV5VHllZFlDZkdPTGUwS1JTUUlRNlNOWkozdHhQMG9RU3RXSlllMFZUS25kOEY1VDRBRWVMLWRXNmowTlA5X3dEQUFBfjCThJ/qBTgNQJVO"

            }
            response = requests.get(self.base_url.format(self.offset), headers=self.headers)
            print(self.base_url.format(self.offset))
            if 200 == response.status_code:
               self.parse_data(response.text)
        except Exception as e:
            print(e)
            time.sleep(2)
            pass

    def parse_data(self, responseData):

            all_datas = json.loads(responseData)

            if 0== all_datas['ret']:

                summy_datas = all_datas['general_msg_list']
                datas = json.loads(summy_datas)['list']
                for data in datas:
                    try:
                        title = data['app_msg_ext_info']['title']
                        title_child = data['app_msg_ext_info']['digest']
                        article_url = data['app_msg_ext_info']['content_url']
                        cover = data['app_msg_ext_info']['cover']
                        print(title,title_child,article_url,cover)
                    except Exception as e:
                        print(e)
                        continue


                print('----------------------------------------')
                time.sleep(3)
                self.offset = self.offset+10
                self.request_data()
            else:
                print('抓取数据出错！')



if __name__ == '__main__':
    d = mp_spider()
    d.request_data()