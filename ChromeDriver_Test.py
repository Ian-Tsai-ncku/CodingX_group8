# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:23:55 2020

@author: 蔡丞益
"""

from selenium import webdriver
import time
import csv

# if putting the chromedriver in diff place, it is neccessary to imply where it is 
chromedriver = 'D:/ChromeDriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://bhuntr.com/tw/competitions/wall')
time.sleep(3)

# scroll down to the end of the page, the for-loop is for the pages will read more when hitting the end of the page
for i in range(15):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
htmltext = driver.page_source

# get the tilte for all the contest
from bs4 import BeautifulSoup
soup = BeautifulSoup(htmltext,'lxml')
info = soup.find_all('div',class_='card__content pull-left')
# for i in info:
#     print(i.text)

# try to find out all the links
def Find_href(info,element):
    lists = []
    for i in info:
        elements = i.find(element).get('href')       
        lists.append(elements)
    return lists

# 'a' element is usually where the links are
link_list = Find_href(info,'a')

# print out all the links(this is for checking whether getting the links)
# for i in link_list:
#     print(i)

# save all the links as csv file
with open('links.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(link_list)