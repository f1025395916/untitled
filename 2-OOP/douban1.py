import requests
import  bs4
import re

res = requests.get("https://movie.douban.com/top250")
soup = bs4.BeautifulSoup(res.text,"html.parser")
# class为类关键词，所以用class_代替
targets = soup.find_all("div",class_="hd")
for each in targets:
    print(each.a.span.text)


