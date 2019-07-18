from urllib import request
from bs4 import BeautifulSoup
import  re
url="http://www.baidu.com"

req = request.urlopen(url)
content = req.read()

soup = BeautifulSoup(content,'lxml')

# bs自动转码


print(soup.prettify())

titles = soup.select("title")
print(titles)
print(type(titles))
print(titles[0])
print("***"*12)

metas = soup.select("meta[content='always']")

print(metas)



#tag两个重要的标签
# -name
# -