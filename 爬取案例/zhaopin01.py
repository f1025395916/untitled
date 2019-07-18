# 请求地址
# https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&_v=0.25338392&x-zp-page-request-id=60c23897d8d94bd4963ef9e4a6427708-1562576503846-25717&x-zp-client-id=16e6accc-34d6-45ef-a286-1b91478553eb

import urllib.request
import json
import jsonpath
import xlwt


myxls = xlwt.Workbook()
# 创建一个worksheet
sheet1 = myxls.add_sheet(u'yx',cell_overwrite_ok=True)

# write(i,j,u) 存取文档的首行
sheet1.write(0,1,"公司名")
sheet1.write(0,2,"地区")
sheet1.write(0,3,"公司人数")
sheet1.write(0,4,"公司类型")
sheet1.write(0,5,"公司网站")
sheet1.write(0,6,"岗位需求")
sheet1.write(0,7,"要求毕业性质")
sheet1.write(0,8,"薪资")
sheet1.write(0,9,"工作性质")
sheet1.write(0,10,"福利")
sheet1.write(0,11,"工作名字")

def openurl(pageCount,keyWord):
    n = 0
    for i in range(1,pageCount):
        #url3 = "https://fe-api.zhaopin.com/c/i/sou?start="+str(i*90)+"&pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&_v=0.25338392&x-zp-page-request-id=60c23897d8d94bd4963ef9e4a6427708-1562576503846-25717&x-zp-client-id=16e6accc-34d6-45ef-a286-1b91478553eb"
        url3=  "https://fe-api.zhaopin.com/c/i/sou?start="+str(i*90)+"&pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw="+str(keyWord)+"&kt=3&=0&_v=0.10225945&x-zp-page-request-id=d65e4c86a0134385a1fe1ed796170184-1562655053938-947699&x-zp-client-id=16e6accc-34d6-45ef-a286-1b91478553eb"
        req = urllib.request.Request(url3)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
        data = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(data)
        # 工作名字
        jobName = jsonpath.jsonpath(data,'$..jobName')
        # 工作类型
        jobType = jsonpath.jsonpath(data,'$..jobType.items[0].name')

        # 获取公司
        company = jsonpath.jsonpath(data,'$..company')
        # 公司名字
        companyName= jsonpath.jsonpath(data,'$..company.name')
        # 公司人数
        companyPeopleNumber = jsonpath.jsonpath(data,'$..company.size.name')
        # 公司类型
        companyType = jsonpath.jsonpath(data,'$..company.type.name')
        # 公司网址
        companyUrl = jsonpath.jsonpath(data,'$..company.url')
        # 城市
        city = jsonpath.jsonpath(data,'$..city')
        # 城市名字
        cityName = jsonpath.jsonpath(data,'$..city.items[0].name')
        # 工作经验
        workingExp = jsonpath.jsonpath(data, "$..workingExp")
        workingExpName = jsonpath.jsonpath(data, "$..workingExp.name")
        # 教育
        eduLevel = jsonpath.jsonpath(data, '$..eduLevel')
        eduLevelName = jsonpath.jsonpath(data,'$..eduLevel.name')
        # 公司福利
        welfare = jsonpath.jsonpath(data,"$..welfare")
        # 薪资
        salary =jsonpath.jsonpath(data,'$..salary')
        # 兼职全职
        emplType = jsonpath.jsonpath(data,"$..emplType")
        for i in range(0,90):


            print("公司编号："+str(n))
            print(company[i])
            print(cityName[i])
            print(companyPeopleNumber[i])
            print(companyType[i])
            print(companyUrl[i])
            print(workingExpName[i])
            print(jobName[i])
            print(jobType[i])
            print(eduLevelName[i])

            print(welfare[i])
            print(emplType[i])
            print()
            n = n+1
            #sheet1.write(行，列，"")
            sheet1.write(n, 0, n)
            sheet1.write(n, 1, companyName[i])
            sheet1.write(n, 2, cityName[i])
            sheet1.write(n, 3, companyPeopleNumber[i])
            sheet1.write(n, 4, companyType[i])
            sheet1.write(n, 5, companyUrl[i])
            sheet1.write(n, 6, jobType[i])
            sheet1.write(n, 7, eduLevelName[i])
            # sheet1.write(n,8,welfare[i])
            sheet1.write(n, 8, salary[i])
            sheet1.write(n, 9, emplType[i])
            sheet1.write(n, 10, welfare[i])
            sheet1.write(n, 11, jobName[i])

    myxls.save('zhaopin-.net.xls')


if __name__ =="__main__":
    openurl(2,".net")










