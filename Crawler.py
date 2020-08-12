# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:36:13 2020

@author: ian05
"""
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('F:\CodingX\FinalProject\chromedriver.exe')
driver.get('https://bhuntr.com/tw/competitions/wall')
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'lxml')
# print(soup.prettify())
titles = soup.find_all('div',class_='card__content pull-left')
### test to get href
# num=len(titles)
# print(num)
# for i in range(5):
#     ele = titles[i].find('a').get('href')
#     print(ele)
# flag = driver.find_elements_by_xpath('//*[@id="content-div"]/div/section/div/div/div/div[31]/button')
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
time.sleep(3)
start_search_btn = driver.find_elements_by_xpath('//*[@id="content-div"]/div/section/div/div/div/div[31]/button')[0]
for i in range(15):
    start_search_btn.click()
    time.sleep(3)
