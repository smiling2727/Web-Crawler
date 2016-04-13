# -*- coding:utf-8 -*-  
from bs4 import BeautifulSoup
import urllib2  
import sys
import re
'''
Created on 2016年4月12日

@author: Smiling
'''

reload(sys)
#sys.getdefaultencoding()
sys.setdefaultencoding('utf8')  #这一句没错
web_path = 'http://invest.ppdai.com/loan/info?id=1005137'
req = urllib2.Request(web_path)  
response = urllib2.urlopen(req)  
page = response.read()  
#print the_page
response.close()
soup=BeautifulSoup(page, "html.parser") 
print type(soup) 
print soup.prettify()

