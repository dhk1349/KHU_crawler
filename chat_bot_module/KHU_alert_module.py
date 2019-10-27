# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

from flask import Flask, request, jsonify, g, render_template
import KHU_crawler.crawler_module as module
import datetime
import json


app=Flask(__name__)

today=str(datetime.datetime.now())
today1=today[0:10]
today2=today[0:10].replace("-",".")

@app.route('/')
def index_page():
	return render_template("index.html")

@app.route('/swedu')
def SWedu():
	response={'content':module.SWedu(today1)} # 사업단 공지사항
	response=json.dumps(response, ensure_ascii=False).encode('utf8')
	return response

@app.route('/kic')
def kic():
	response={'content':module.KIC(today2)}
	indata=response['content']
	return render_template("kic.html", inlist=indata)

@app.route('/softkhu')
def Softkhu():
	response={'content':module.SoftwareKHU(today1)}
	return response

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
