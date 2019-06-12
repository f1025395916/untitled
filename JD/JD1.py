import requests
import json
import re
import csv

dnbg = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=29&_=1495211171059'  # 电脑办公
shdq = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=19&_=1495250002658'  # 生活电器
sjtx = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=30&_=1495251020781'  # 手机通讯
djd = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=25&_=1495251044176'  # 大家电
znsm = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=31&_=1495251057993'  # 智能数码
yljs = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=45&_=1495251084828'  # 饮料酒水
jjjz = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=37&_=1495251148047'  # 家具家装
mytz = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=43&_=1495251122767'  # 母婴童装
spsx = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=44&_=1495250603966'  # 食品生鲜
ghjq = 'https://ai.jd.com/index_new?app=Seckill&action=pcSeckillCategoryGoods&callback=pcSeckillCategoryGoods&id=32&_=1495251170952'  # 个护家清


def jdmiaosha(url):  # 开始只是想爬去电脑办公的 函数是后来加上去的

    resp = requests.get(url).text
    # print(resp)
    resp = re.findall(r'\((.+)\)', resp)[0]  # 提取纯json代码 不然解析会出错
    # print(resp)
    s = json.loads(resp)
    with open("jd.csv", "a", newline="") as datacsv:
        csvwriter = csv.writer(datacsv, dialect=("excel"))
        csvwriter.writerow(["商品", "价格", "销售状态", "链接"])
    datacsv.close
    for i in s['goodsList']:
        sales_url = "https://item.jd.com/" + str(i['wareId']) + ".html"
        if 'soldRate' in i.keys():
            sales_status = str(i['soldRate']) + "%"  # 区别是否开抢   确定销售状态
        else:
            if not i['startTimeContent']:
                sales_status = "---"
            else:
                sales_status = i['startTimeContent']
        print(
            '商品：{0}\t价格：{1}\t销售状态:{2}\t链接:{3}.'.format(i['wname'], i['miaoShaPrice'], sales_status, sales_url))  # 格式化输出
        with open("jd.csv", "a", newline="") as datacsv:  # 写入到csv文件
            csvwriter = csv.writer(datacsv, dialect=("excel"))
            csvwriter.writerow([i['wname'], i['miaoShaPrice'], sales_status, sales_url])


for url in [dnbg, shdq, sjtx, djd, znsm, yljs, jjjz, mytz, spsx, ghjq]:
    jdmiaosha(url)