# -*- coding:utf-8 -*-  
'''
Created on 2016年4月12日

@author: Smiling
'''
from webcatch import catch

file_path = '/Users/Smiling/Desktop/PythonCatch/test_catch.txt'
catch.printTitle(file_path)
for i in range (10000000,10005000):
    #10001442么有
    web_path = 'http://invest.ppdai.com/loan/info?id='+str(i)
    soup = catch.connectInternet(web_path)
    catch.catchContent(soup, file_path,i)
    print 'OK'



