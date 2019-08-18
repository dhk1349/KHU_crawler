# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:28:16 2019

@author: dhk13
"""

from bs4 import BeautifulSoup as soup
import requests
import datetime

def SWedu():
    url="http://swedu.khu.ac.kr/board5/bbs/board.php?bo_table=06_01"
    html=requests.get(url).text
    obj=soup(html, "html.parser")

    table=obj.find("div", {"class":"colgroup"}).find("div",{"id":"bo_list"}).find("form",{"id":"fboardlist"}).find("tbody").findAll("tr")

    for i in table:
        title=i.find("td", {"class":"td_subject"})
        date=i.find("td",{"class":"td_datetime"}).text.strip()
        title=title.find("div",{"class":"bo_tit"})
        title=title.find("a").text.strip() #제목
        print(title,"  ",date)


def KIC():
    url="http://kic.khu.ac.kr/notice/undergraduate/"
    html=requests.get(url).text
    obj=soup(html, "html.parser")

    table=obj.find("body").find("article").find("div", {"class":"kboard-list"}).findAll("tr")
    table=table[1:]
    for row in table:
        title=row.find("td",{"class":"kboard-list-title"}).find("a").find("div",{"class":"kboard-default-cut-strings"}).text.strip()

        date=row.find("td",{"class":"kboard-list-date"}).text.strip()
        print(title,"   ",date)    

def SoftwareKHU():
    url="http://software.khu.ac.kr/board5/bbs/board.php?bo_table=05_01"
    html=requests.get(url).text
    obj=soup(html, "html.parser")

    table=obj.find("div",{"class":"sContainer"}).find("tbody").findAll("tr")

    for row in table:
        title=row.find("div",{"class":"bo_tit"}).text.strip()    
        date=row.find("td",{"class":"td_datetime"}).text.strip()
        print(title,"   ",date)  

SWedu() # 사업단 공지사
KIC() #국제대학 공지사항
SoftwareKHU()#소프트웨어 중심대학 공지사항

dt=datetime.datetime.now()
print(dt.year," ",dt.month," ",dt.day)