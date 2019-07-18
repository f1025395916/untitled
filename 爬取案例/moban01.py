import requests
from lxml import etree
import pymysql


url = "http://www.cssmoban.com/tags.asp"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
req = requests.get(url,headers=headers)
html = etree.HTML(req.content)

htmldata = html.xpath('//div[@class="pbutton show-tags clearfix"]/a/text()')



# 向mysql插入数据
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='cssmoban')
cursor =db.cursor()


insert_sql = 'insert into tags(tagName) values (%s)'
result  = cursor.executemany(insert_sql,htmldata)

db.commit()
print(result)

# 查询
sql = 'select * from tags'
cursor.execute(sql)
print(cursor.fetchall())


cursor.close()
db.close()



#  moban表字段

# id   模板ID  模板名字  模板链接   在线预览链接   zip下载地址   图片路径