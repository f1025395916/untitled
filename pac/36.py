
from selenium import webdriver
import time

#通过keys模拟键盘

from selenium.webdriver.common.keys import   Keys

# 操作那个浏览器就对那个浏览器建一个实例

driver = webdriver.Chrome()

#driver = webdriver.Firefox()

#自动按照环境变量查找相应的浏览器 ·需要制定浏览器的位置

driver.get("http://www.baidu.com")

# 通过函数查找title标签
print("title:{0}".format(driver.title))

