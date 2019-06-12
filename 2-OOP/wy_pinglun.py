import requests
import bs4
import  json
# 解析json
def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments =comments_json['hotComments']
    with open('hot_comments.txt','w',encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname']+':\n\n')
            file.write(each['content']+'\n')
            file.write("--------------------\n")
def get_comments_others(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['comments']
    with open('comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + ':\n\n')
            file.write(each['content'] + '\n')
            file.write("--------------------\n")

def get_comments(url):
    name_id = url.split('=')[1]
    headers ={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
              'referer':"https://music.163.com/#/song?id=18611546"}

    params = "GBHFWNJ1P/skodKkrBYZstEfnr8eP8XqM3SgZ+yeTGYwYQ4MF9A6lDcbN1rsNGCz08TL/KrLCgkObGMC8Q+LSV6MIJYqZd3dLsVzdcrksLduCfvl/9D4puG5qwajGDceBX441jrdP9raLX6IaYfsO+J0JKWujOV/fkr3VPW4ahowOT2hfKctTWv6qkCll6PaZchdmRac9cpXKju9bkwtN/xqDZJq1ixzxI0QubUro4o="
    encSecKey="0f3c8f16b58eaa7c3f37e854ae21cd5c88f205a4f46498208698c8b0f520be338b7a82edfbdd2662180b635624f9cd37d32d565da6945772aa873679d291640a439b8bf518e16da21d46add3ffaef801e13969ac47ea5ccb508cfa2d8d1d51b475189924a3cc11186f2efd238cb397b77ceff766200337a9a062ab802b0714b8"

    data ={
        "params":params,
        "encSecKey":encSecKey
        }
    target_url ="https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token".format(name_id)
    res =requests.post(target_url,headers=headers,data=data)
    return res

def main():
    url =input("请输入链接地址:")
    res =get_comments(url)
    get_hot_comments(res)
    get_comments_others(res)
    with open("wypinglun.txt","w",encoding="utf-8") as file:
        file.write(res.text)

if __name__=="__main__":
    main()