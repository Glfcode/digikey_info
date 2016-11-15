# _*_ coding:utf-8 _*_

import urllib
from bs4 import BeautifulSoup
from url import html_read

url1 = "http://www.digikey.cn"

#打开一级网页
html_doc1 = html_read(url1)

#获取二级网页链接
soup1 = BeautifulSoup(html_doc1)
html_href = soup1.find(id='header_0_mobileheadernav_0__mobileListItems__subHyperLinks_0__subMenuHyperLinks_1__subMenuHyperLinks_2')
href1 = html_href.get('href')
url2 = url1+href1

#打开二级网页
html_doc2 = html_read(url2)

#获取三级网页链接
soup2 = BeautifulSoup(html_doc2).find_all('a')
for x in soup2:
    if x.get('cookie-tracking') == 'part_family=' + u'可调电感器;':
        link1 = x.get('href')
    else:
        pass
url3 = url1+link1

#打开三级网页
html_doc3 = html_read(url3)

def Save_file(file_name,str):
    """
    追加模式保存数据
    :param file_name:文件名
    :param str:待保存数据
    :return:
    """
    fp = open(file_name,'a+')
    fp.write(str+'\n')
    fp.close()

#抓取页面信息共三页（元器件链接）
soup3 = BeautifulSoup(html_doc3).find_all('td',class_='tr-image')
for x in soup3:
    link2 = x.find('a').get('href')
    url4 = url1+link2
    Save_file('digikey.txt',url4)
    # print url4
print '第1页抓取完成！'

for i in xrange(2,4,1):
    url = url3+'/page/%s'%(str(i))
    html_new2 = urllib.urlopen(url)
    html_doc3 = html_new2.read()
    soup3 = BeautifulSoup(html_doc3).find_all('td',class_='tr-image')
    for x in soup3:
        link2 = x.find('a').get('href')
        url4 = url1+link2
        Save_file('digikey.txt',url4)
        # print url4
    print '第%s页抓取完成！'%(str(i))


