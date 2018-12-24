from pyvirtualdisplay import Display
from selenium import webdriver
display=Display(visible=0, size=(800, 600))# 初始化屏幕
display.start()
driver = webdriver.Chrome()# 初始化Chrome
driver.get('https://tieba.baidu.com/f?fr=wwwt&kw=%E9%9B%BE%E9%9C%BE')
print(driver.title)