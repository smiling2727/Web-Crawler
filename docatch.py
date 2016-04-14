# -*- coding:utf-8 -*-  
'''
Created on 2016年4月12日

@author: Smiling
'''
from webcatch import catch

file_path = '/Users/Smiling/Desktop/PythonCatch/test_catch.txt'
catch.printTitle(file_path)
for i in range (10005994,10006000):
    web_path = 'http://invest.ppdai.com/loan/info?id='+str(i)
    try:
        soup = catch.connectInternet(web_path)
        catch.catchContent(soup, file_path,i)
        print 'OK'
    except:
        print 'Content Error'




