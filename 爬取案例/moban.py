import requests
from lxml import etree

class Mobanzhijia(object):
    def __init__(self,themes):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        self.themes_url = "http://www.cssmoban.com/tags.asp?n={}".format(themes) # 设置需要查找的主题链接
        self.single_url = "http://www.cssmoban.com"  #将要与每个模板单独拼接的网站
        self.page_url = "http://www.cssmoban.com/tags.asp" #将要每一页模板拼接的网站
        self.page_url_o = None   #初始化每页需拼接的内容
        self.themes_url_list =[]    # 链接初始化列表，用来存放链接
        self.themes_zip_list = []    # zip包初始化列表，用来存放zip包链接
        self.moban_zipName_list =[]     # 模板名字初始化列表，用来存放模板zip的名字
        self.moban_imageUrl_list =[]   # 单独存放图片链接
        self.tagsDict ={}      # 初始化关键词dict
        self.themes_images ={} # 初始化图片dict
        self.themes_onlineUrl ={} # 初始化在线预览链接dict
    def get_page_url(self):
        page_response = requests.get(self.themes_url,headers = self.headers)
        page_html = etree.HTML(page_response.content)
        self.page_url_o = page_html.xpath('//div[@class="tagsPage"]/form/a[text()="下一页"]/@href') #判断下一页的链接是否为空
        # 判断是否为空，为空则获取的最后一页
        if not self.page_url_o:
            return
        self.themes_url = self.page_url_o[0]
        self.get_moban_url_list()

    # 获取themes_url 页中所有模板的网页
    def get_moban_url_list(self):
        themes_response = requests.get(self.themes_url,headers = self.headers)
        themes_html = etree.HTML(themes_response.content)
        #模板链接
        moban_url_list  = themes_html.xpath('//ul[@class="thumbItem large clearfix"]/li/a/@href')
        for url in moban_url_list:
            self.themes_url_list.append(self.single_url+url)
        self.get_moban_zip()

    # 获取themes_url链接中所有zip文件的下载地址
    def get_moban_zip(self):
        for i in self.themes_url_list:
            moban_response = requests.get(i,headers=self.headers)
            moban_html = etree.HTML(moban_response.content)
            moban_zip = moban_html.xpath('//div[@class="btn"]/a[2]/@href')
            moban_name =moban_html.xpath('//h1/text()')
            self.themes_zip_list.append(moban_zip[0])
            self.moban_zipName_list.append(moban_name[0])

            # 获取关键词
            moban_tags = moban_html.xpath('//div[@class="tags"]/a/text()')
            # 关键词存放dict
            self.tagsDict[str(moban_name)] = moban_tags
            # 获取图片链接
            moban_image = moban_html.xpath('//div[@class="large-Imgs"]/img/@src')
            # 图片链接存放dict
            self.themes_images[str(moban_name)] = moban_image
            # 图片链接存放数组
            self.moban_imageUrl_list.append(moban_image[0])
            # 获取在线预览链接
            moban_onlineUrl = moban_html.xpath('//div[@class="btn"]/a[1]/@href')
            # 在线预览链接存放dict
            self.themes_onlineUrl[str(moban_name)] = moban_onlineUrl




        print(self.themes_zip_list)
        print(self.moban_zipName_list)
        print(self.tagsDict)

        print(self.themes_images)  # 图片链接
        print(self.themes_onlineUrl)  # 在线预览链接


        # 模板的数量
        print(len(self.moban_zipName_list))
        # tags字典的数量
        print(len(self.tagsDict))




        self.get_write()




    def get_write(self):
        # 将所有zip文件下载
        '''
        for index,i in  enumerate(self.themes_zip_list):
            zip_response = requests.get(i,headers = self.headers)
            with open("F:\\zip\\"+str(self.moban_zipName_list[index])+".zip","wb") as f:
                f.write(zip_response.content)
        '''
        # 将模板图片下载
        for index,i in enumerate(self.moban_imageUrl_list):
            image_response = requests.get(i,headers = self.headers)
            with open("F:\\images\\"+str(self.moban_zipName_list[index])+".jpg","wb") as f:
                f.write(image_response.content)



        # 清空列表准备保存下一页内容
        self.themes_url_list =[]
        self.themes_zip_list=[]
        self.moban_zipName_list=[]

        #self.get_page_url()
themes = input("input:") #输入想要获取模板的类型
spider = Mobanzhijia(themes)
spider.get_moban_url_list()








