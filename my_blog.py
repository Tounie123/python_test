from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import ssl

context = ssl._create_unverified_context()

resp=urlopen('https://weibo.com/1826499614/follow?rightmod=1&wvr=6',context=context)
print(resp)
print("zane")
soup=BeautifulSoup(resp,'html.parser')
print(soup)
fans = tagToday=soup.find('ul',class_="member_li")
'''
try:
    temperatureHigh=fans.span.string  #有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
except AttributeError as e:
    temperatureHigh=fans.find_next('p',class_="member_li S_bg1").span.string  #获取第二天的最高温度代替
'''
print(fans)