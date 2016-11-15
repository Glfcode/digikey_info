# _*_ coding:utf-8 _*_

import urllib

def html_read(url):
    """
    读取网页源代码
    :param url: url地址
    :return: 源代码
    """
    html = urllib.urlopen(url)
    code = html.read()
    return code

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
