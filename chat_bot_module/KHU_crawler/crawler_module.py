# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:28:16 2019

@author: dhk13
"""

from bs4 import BeautifulSoup as soup
import requests
import datetime

def SWedu(today1):
    url="http://swedu.khu.ac.kr/board5/bbs/board.php?bo_table=06_01"
    html=requests.get(url).text
    obj=soup(html, "html.parser")

    table=obj.find("div", {"class":"colgroup"}).find("div",{"id":"bo_list"}).find("form",{"id":"fboardlist"}).find("tbody").findAll("tr")
    newsbox=[]
    for i in table:
        date=i.find("td",{"class":"td_datetime"}).text.strip()
        if(date==today):
            title=i.find("td", {"class":"td_subject"})
            title=title.find("div",{"class":"bo_tit"})
            title=title.find("a").text.strip() #제목
            newsbox.append(title)
    if(len(newsbox)==0):
        newsbox.append("No New Issue on SW중심사업단\n")
    return newsbox

def KIC(today2):
    url="http://kic.khu.ac.kr/notice/undergraduate/"
    html=requests.get(url).text
    obj=soup(html, "html.parser")

    table=obj.find("body").find("article").find("div", {"class":"kboard-list"}).findAll("tr")
    table=table[1:]
    newsbox=[]
    for row in table:
        date=row.find("td",{"class":"kboard-list-date"}).text.strip()
        if(date==today):
            title=row.find("td",{"class":"kboard-list-title"}).find("a").find("div",{"class":"kboard-default-cut-strings"}).text.strip()
            newsbox.append(title)
    if(len(newsbox)==0):
        newsbox.append("No NEW Issue on KIC\n")
    return newsbox

def SoftwareKHU(today1):
    url="http://software.khu.ac.kr/board5/bbs/board.php?bo_table=05_01"
    html=requests.get(url).text
    obj=soup(html, "html.parser")

    table=obj.find("div",{"class":"sContainer"}).find("tbody").findAll("tr")
    newsbox=[]
    for row in table:
        date=row.find("td",{"class":"td_datetime"}).text.strip()
        if(date==today1):
            title=row.find("div",{"class":"bo_tit"}).text.strip()
            newsbox.append(title)
    if(len(newsbox)==0):
        newsbox.append("No New Issue on SW융합대학\n")
    return newsbox
'''
dt=datetime.datetime.now()
today=str(dt)
today1=today[0:10]
today2=today[0:10].replace("-",".")
print(SWedu(today1)) # 사업단 공지사
print(KIC(today)) #국제대학 공지사항
print(SoftwareKHU(today))#소프트웨어 중심대학 공지사항
'''
