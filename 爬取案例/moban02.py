import requests
from lxml  import etree
import  re
import pymysql

url = "http://www.cssmoban.com/cssthemes/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

single_url = "http://www.cssmoban.com"  #将要与每个模板单独拼接的网站


db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='cssmoban')
cursor = db.cursor()

moban_Id_list = []      # 模板ID
moban_title_list = []   # 模板名字
moban_url_list = []     # 模板链接
moban_onlineUrl_list = []  # 模板在线预览
moban_imageUrl_list= []    # 素略图
moban_zip_list = []     # zip包
page_url_o = None       # 分页
page_url_list =[]
moban_tags_list = []  # 关键词
moban_tagsId_list= []   # 关键词ID
moban_list =[]   # 二维列表
tagsId = []
tagsIds = []

pageCount=0

def get_page_url():
    page_response = requests.get(url,headers =headers)
    page_html = etree.HTML(page_response.content)
    text = page_html.xpath('//td[@id="pagelist"]/span/text()')
    ret = re.findall(r'\d+',str(text))
    #for i in range(1,int(ret[0])):
    for i in range(1, 10):
        mobanUrl = "http://www.cssmoban.com/cssthemes/index_"+str(i)+".shtml"
        page_url_list.append(mobanUrl)

   # page_url_list.append("http://www.cssmoban.com/cssthemes/")
def getmobanContent():
    for i in page_url_list:
        page_response = requests.get(i)
        page_html = etree.HTML(page_response.content)
        #一个列表页的链接
        mobanUrl = page_html.xpath('//ul[@class="thumbItem large clearfix"]/li/a/@href')# 注意：xpath返回的List

        mobanUrl.reverse()
        for index, i in enumerate(mobanUrl):
            mobanUrl[index] = single_url + i
            # 模板ID
            ret = re.findall(r'\d+', str(mobanUrl[index]))
            moban_Id_list.append(int(ret[0]))     # 模板ID list


            moban_url_list.append(mobanUrl[index])  # 链接  list




    for index,i in enumerate(moban_url_list):
        moban_response = requests.get(moban_url_list[index],headers=headers)
        moban_html = etree.HTML(moban_response.content)
        mobanTitle = moban_html.xpath('//div[@class="con-right"]/h1/text()')

        moban_title_list.append(mobanTitle[0])  # 标题 list

        mobanOnline = moban_html.xpath('//div[@class="btn"]/a[1]/@href')

        moban_onlineUrl_list.append(mobanOnline[0])   # 在线预览  list

        mobanZipUrl = moban_html.xpath('//div[@class="btn"]/a[2]/@href')

        moban_zip_list.append(mobanZipUrl[0])     # zip包地址  list

        mobanTags = moban_html.xpath('//div[@class="tags"]/a[position()<(last())]/text()')

        moban_tags_list.append(mobanTags)    #  关键词

        mobanImageUrl  = moban_html.xpath('//div[@class="large-Imgs"]/img/@src')

        moban_imageUrl_list.append(mobanImageUrl[0])  # image  list


    #getTagsId()


    addMysql()

def addMysql():

    insert_sql = "insert into moban(mobanId,title,onlineUrl,zipUrl,url,imageUrl) values (%s,%s,%s,%s,%s,%s)"
    moban_list = list(zip(moban_Id_list, moban_title_list, moban_onlineUrl_list, moban_zip_list, moban_url_list, moban_imageUrl_list))


    try:
       cursor.executemany(insert_sql, moban_list)
       #cursor.executemany(insert_sql, moban_Id_list,moban_title_list,moban_onlineUrl_list,moban_zip_list,moban_url_list,moban_imageUrl_list)

    except Exception as e:
        print(e)
    else:
        db.commit()
        print("事务处理成功",cursor.rowcount)

    # 查询
    sql = 'select * from moban'
    cursor.execute(sql)
    print(cursor.fetchall())

    cursor.close()
    db.close()
    # 根据tagsName获取tagsId
def getTagsId():

    tagsIdList=[]
    list1=[]
    print(len(moban_Id_list))
    print(len(moban_tags_list))
    print(moban_Id_list)
    print("***"*12)
    print(moban_tags_list)

    for i,(tags,mobanId) in enumerate(zip(moban_tags_list,moban_Id_list)):
        tagsIdList.clear()
        for i2 in tags:
            sql = "select tags.Id  from tags where tagName= '" + str(i2)+"'"

            #print(tags)
            #['二栏', '商务模版', '粉色', '网店', '内衣']
            #print(sql)
            #select tags.Id  from tags where tagName= '二栏'
            cursor.execute(sql)
            items = cursor.fetchone()

            for row in items:
                tagsId = row

            tagsIdList.append(tagsId)

        print(tagsIdList)
        for index,id in enumerate(tagsIdList):
            currentId = moban_Id_list[i]
            currentTagsId = id
            #向联合表moban_tags插入数据
            cursor.execute("insert into moban_tags(mobanId,tagId) values (%s,%s)",(currentId,currentTagsId))
            db.commit()








if __name__ == '__main__':
    get_page_url()
    getmobanContent()







