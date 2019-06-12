#!/usr/bin/python
# -*- coding: UTF-8 -*-
# made in white-night
# coding=utf-8

import re
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtWidgets
from selenium import webdriver
import datetime
import time
import threading
import wmi


class LoginDlg(QDialog):
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)

        usr = QLabel("请选择抢购方式：")
        pwd = QLabel("请输入抢购时间：")
        self.lineEdit = QLineEdit("", self)
        self.lb0 = QLabel("请输入待抢购网址：", self)
        self.lbl = QLabel("等待选择抢购方案", self)
        self.lb2 = QLabel("机器码：", self)
        self.lb3 = QLabel("授权码：", self)
        self.lb4 = QLabel("（获取授权请加群：462510942）", self)
        self.lb5 = QLabel("（请勿更改机器码，否则无法授权）", self)
        self.lineEdit2 = QLineEdit("", self)
        self.lineEdit1 = QLineEdit("", self)
        self.combo = QComboBox(self)
        self.combo.addItem("0、请选择抢购方案")
        self.combo.addItem("1、加购物车")
        self.combo.addItem("2、不加购物车")
        self.combo.addItem("3、抢购优惠券")

        # self.lineEdit.move(200,100)
        self.lb0.move(50, 100)
        self.lbl.move(50, 150)
        self.lb2.move(50, 200)
        self.lb3.move(50, 250)
        self.lb4.move(250, 250)
        self.lb5.move(250, 200)
        self.lineEdit2.move(100, 200)
        self.lineEdit1.move(100, 250)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()
        self.dateTimeEdit = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit.setGeometry(QtCore.QRect(140, 50, 121, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 11, 1), QtCore.QTime(9, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(pwd, 1, 0, 1, 1)
        gridLayout.addWidget(self.lb0, 2, 0, 1, 1)
        gridLayout.addWidget(self.combo, 0, 1, 1, 3)
        gridLayout.addWidget(self.dateTimeEdit, 1, 1, 1, 3)
        gridLayout.addWidget(self.lineEdit, 2, 1, 1, 3)

        sqBtn = QPushButton("授权")
        okBtn = QPushButton("确定")
        cancelBtn = QPushButton("关闭软件")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)
        btnLayout.addWidget(sqBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)
        sqBtn.clicked.connect(self.cpuid)
        self.setWindowTitle("VN辅助抢购软件")
        self.resize(600, 400)

        self.thread_handle = None

    def thread_function(self, index):
        # 需要在线程加一个全局变量的判断 用于终止死循环 用来切换方案
        data = self.cpuid1[2] + self.cpuid1[5] + min(self.cpuid1) + self.cpuid1[-5] + self.cpuid1[1] + self.cpuid1[3] + \
               self.cpuid1[4] + max(self.cpuid1) + self.cpuid1[1] + \
               self.cpuid1[-1] + self.cpuid1[-3] + "V" + "N" + self.cpuid1[-2] + self.cpuid1[0] + self.cpuid1[-4]
        print(data)
        if self.lineEdit1.text() == data and self.lineEdit2.text() == self.cpuid1:
            if index == 0:
                self.lbl.setText("请选择抢购方案，然后点击确定")
            elif index == 1:
                self.lbl.setText("成功调用加购物车方案")
                self.gouwubuy()
            elif index == 2:
                self.lbl.setText("成功调用不加购物车方案")
                self.buy()
            else:
                self.lbl.setText("成功调用抢券方案")
                self.quanbuy()
        else:
            self.lbl.setText("请输入正确的授权码")

    def accept(self):
        # 线程创建
        self.thread_handle = threading.Thread(target=LoginDlg.thread_function, args=(self, self.combo.currentIndex()))
        self.thread_handle.start()
        return

    def gouwubuy(self):
        browser.get("https://cart.taobao.com/cart.htm")
        # 点击购物车里全选按钮
        buyt = self.dateTimeEdit.text()
        buyti = re.findall(" (.*)", buyt)
        buytime = buyti[0] + ":00.000000"
        while True:
            now = datetime.datetime.now().strftime('%H:%M:%S.%f')
            # 对比时间，时间到的话就点击结算
            if now > buytime:
                # 点击结算按钮
                try:
                    if browser.find_element_by_id("J_Go"):
                        browser.find_element_by_id("J_Go").click()
                except:
                    pass
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        self.lbl.setText("提交订单时间为：%s" % now1)
                except:
                    pass

    def buy(self):
        browser.get(self.lineEdit.text())
        while True:
            try:
                if browser.find_element_by_link_text('立即购买'):
                    browser.find_element_by_link_text('立即购买').click()
            except:
                pass
            try:
                if browser.find_element_by_link_text('提交订单'):
                    browser.find_element_by_link_text('提交订单').click()
                    now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    self.lbl.setText("提交订单时间为：%s" % now1)
                    break
            except:
                pass

    def quanbuy(self):
        browser.get(self.lineEdit.text())
        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            # 对比时间，时间到的话就点击结算
            try:
                if browser.find_element_by_link_text('立刻抢'):
                    browser.find_element_by_link_text('立刻抢').click()
            except:
                pass
            try:
                if browser.find_element_by_link_text('点击领券'):
                    browser.find_element_by_link_text('点击领券').click()
            except:
                pass

    def cpuid(self):
        w = wmi.WMI()
        cpus = w.Win32_Processor()
        for u in cpus:
            self.cpuid1 = u.ProcessorId
            self.lineEdit2.setText(self.cpuid1)


def login():
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
    time.sleep(3)


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    app = QApplication(sys.argv)
    dlg = LoginDlg()
    dlg.show()
    dlg.exec_()
    app.exit()