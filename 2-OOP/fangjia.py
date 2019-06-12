import  requests
import  bs4
import re
# 生成excel
import openpyxl
def open_url(url):
    headers ={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url,headers=headers)
    return res

def find_data(res):
    data=[]
    soup =bs4.BeautifulSoup(res.text,'html.parser')
    content =soup.find(id="Cnt-Main-Article-QQ")
    target = content.find_all("p",style="TEXT-INDENT: 2em" )


    # 可以用for...in 循环的都是可迭代的，可以用next()方法的才是迭代器，可迭代可以用iter()变成迭代器
    target = iter(target)
    for each in target:
        # isnumsoc:判断是否为非数字字符
        if each.text.isnumeric():
            data.append([
                re.search(r'\[(.+)\]',next(target).text).group(1),
                re.search(r'\d.*',next(target).text).group(),
                re.search(r'\d.*',next(target).text).group(),
                re.search(r'\d.*',next(target).text).group()
            ])
    #一定要注意范围，不要把return放在了for循环的里面
    return data

# 生成excel表格
def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws =wb.active
    ws.append(['城市','平均房价',"平均工资","房价工资比"])
    for each in data:
        ws.append(each)
    wb.save("2017全国城市房价 工资排行榜出炉.xlsx")

def main():
    url ="http://news.house.qq.com/a/20170702/003985.htm"
    res = open_url(url)
    result = find_data(res)
    to_excel(result)

if __name__=="__main__":
    main()

