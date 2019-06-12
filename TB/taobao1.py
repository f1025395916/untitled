import  requests


def open_url(keyword):
    # 地址栏的参数
    payload ={"q":"零基础入门学习python","sort":"sale-desc"}
    url = "https://s.taobao.com/search"
    res =requests.get(url,params=payload)
    return res

def main():
    keyword = input("请输入搜索关键词：")
    res =open_url(keyword)

    with open("items.txt","w",encoding="utf-8") as file:
        file.write(res.text)
if __name__ =="__main__":
    main()