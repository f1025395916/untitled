import requests
import bs4
def get_url(url):
    headers ={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res =requests.get(url,headers=headers)
    return res

def main():
    url =input("请输入链接地址:")
    res =get_url(url)

    with open("wangyi.txt","w",encoding="utf-8") as file:
        file.write(res.text)

if __name__=="__main__":
    main()