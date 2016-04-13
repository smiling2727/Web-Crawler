# -*- coding:utf-8 -*-  
'''
Created on 2016年4月12日

@author: Smiling
'''
from bs4 import BeautifulSoup
import urllib2  
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')  #这一句没错(用来避免乱码问题)

def connectInternet(web_path):
    try:
        req = urllib2.Request(web_path)  
        response = urllib2.urlopen(req)  
        page = response.read()  
        response.close()
        soup=BeautifulSoup(page, "html.parser")  
        return soup
    except:
        print 'Internet error'
    

def printTitle(file_path):
    myfile = open(file_path,'a')
    myfile.write('ID'+'    '+'题目'+'    '+'评级'+'    '+'成功次数'+'    '+'流标次数'+'    '+'金额'+'    '+'年利率'+'    '+'期限'+'    '+'进度条'+'    '+'投标人数''    '+'结束时间')
    myfile.write('\n')

def catchContent(soup,file_path,i):
    title1 = soup.html.body.find('h3', {'class' : "clearfix"}).text #题目
    credit_rating_ori = soup.html.body.find('span',{'class' : 'creditRating'})
    cr= str(credit_rating_ori)
    cr_all = cr.split(" ")      
    p_rating = re.compile(r'\w+') #匹配到creditRating
    group_cr = p_rating.findall(cr_all[2])
    #print group_cr[0] #评级
    bid_times = soup.html.body.find('span',{'class' : "bidinfo"}).text #1 次成功｜ 0 次流标(非实时)
    p_number = re.compile(r'\d+') #匹配到所有的数字
    group_bidtimes = p_number.findall(bid_times)
    loan_detail = soup.html.body.find('div',{'class':'newLendDetailMoneyLeft'}).text#loan_detail包括金额，年利率，期限
    loan_detail = loan_detail.replace(' ','')#去掉loan_detail里的空格
    loan_detail = loan_detail.replace('\n','')#去掉loan_detail里的换行符
    loan_detail = loan_detail.replace(',','')#去掉loan_detail里的逗号（可能会把数字分开）
    group_loandetail = p_number.findall(loan_detail)
    process_tag = soup.html.body.find('div',{'class':'part clearfix'}).text#进度条
    group_processtag = p_number.findall(process_tag)
    finish_time = soup.html.body.find('span',{'class':'countdown_row countdown_amount'}).text #结束时间
    
    myfile = open(file_path,'a')
    myfile.write(str(i))#ID
    myfile.write('    '+title1.strip())#题目
    myfile.write('    '+group_cr[0])#评级
    myfile.write('    '+group_bidtimes[0])#成功次数
    myfile.write('    '+group_bidtimes[1])#流标次数
    myfile.write('    '+group_loandetail[0])#金额
    myfile.write('    '+group_loandetail[1]+'%')#年利率
    myfile.write('    '+group_loandetail[1])#期限
    myfile.write('    '+group_processtag[0]+'%')#进度条
    myfile.write('    '+group_processtag[1])#投标人数
    myfile.write('    '+finish_time.strip())#结束时间
    myfile.write('\n')


