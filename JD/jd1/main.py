#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant


if __name__ == '__main__':
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆

#加入购物车定时提交订单
def submission_timing():

    asst.clear_cart()       # 清空购物车（可选）
    sku_id =input("请输入商品ID：")
    startTime =input("请输入开始时间")
    asst.add_item_to_cart(sku_ids=sku_id)  # 根据商品id添加购物车（可选）
    # ID：100001324422
    # startTime:2019-07-17 09:45:59.200
    asst.submit_order_by_time(buy_time='', retry=1, interval=5)
    # 5个参数
    # sku_ids: 商品id，多个商品id用逗号进行分割，如"123,456,789"
    # buy_time: 下单时间，例如：'2019-02-19 09:59:59.500'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个



# 定时秒杀(抢购商品)
def secondkill_timing():
    asst.exec_seckill_by_time(sku_ids='100002852990', buy_time='2019-02-19 09:59:59.500', retry=10, interval=4)
    # 5个参数：
    # sku_ids: 商品id，多个商品id用逗号进行分割，如 "123,456,789"
    # buy_time: 下单时间，例如：'2019-02-19 09:59:59.500'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个



