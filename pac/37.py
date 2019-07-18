from selenium import  webdriver
from  selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)

text = driver.find_element_by_id('wrapper').text
print(text)

print(driver.title)

# 得到页面的快照
driver.save_screenshot('index.png')

driver.find_element_by_id('kw').send_keys(u'大熊猫')

# id="su" 是百度搜索的按钮 ·click

driver.find_element_by_id("su").click()

time.sleep(5)
driver.save_screenshot("daxiongmao.png")

# 获取当前页面的cookie
print(driver.get_cookies())

# 模拟输入两个摁键 ctrl + a,选中输入框的全部
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')

# 全部选中之后，剪切  ctrl + x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')


driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.save_screenshot('hangmu.png')

driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot('hangmu2.png')

# 清空输入框，clear
driver.find_element_by_id('kw').clear()
driver.save_screenshot('qingkong.png')

# 关闭浏览器
driver.quit()

