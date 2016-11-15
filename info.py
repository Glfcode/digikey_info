# _*_ coding:utf-8 _*_

from url import *
from bs4 import BeautifulSoup
import time

url = "http://www.digikey.cn"

fh = open('digikey.txt')
lines = fh.readlines()

html = html_read(lines[0])
# print html

soup = BeautifulSoup(html)

#抓取索引
html_index = soup.find(class_="breadcrumbs")
href1 = html_index.find_all('a')
for x in href1:
    Product_index = x.text+' '+url+x.get('href')
    # print type(Product_index)
    Save_file('./info/1.txt',Product_index.encode('utf-8'))

#抓取产品概览
html_overview = soup.find('table',id='product-details').text
# for i in html_overview:
#     print type(i.find('th')),i.find('th')
#     print i.find('td')
Save_file('./info/2.txt',html_overview.replace(' ','').encode('utf-8'))
# print type(html_overview),html_overview.replace(' ','')

infp = open('./info/2.txt', "r+")
lines = infp.readlines()
for li in lines:
    if li.split():
        infp.writelines(li)
        infp.close()