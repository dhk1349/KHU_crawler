# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

from flask import Flask, request, jsonify, g
import KHU_crawler.crawler_module as module
import datetime


app=Flask(__name__)

today=str(datetime.datetime.now())
today1=today[0:10]
today2=today[0:10].replace("-",".")

@app.route('/')
def alert():
	return

@app.route('/swedu')
def SWedu():
    #dt=datetime.datetime.now()
    #today=str(dt)
    #today1=today[0:10]
    #today2=today[0:10].replace("-",".")
    response={'content':module.SWedu(today1)} # 사업단 공지사항
    return response
    #return jsonify(response)

@app.route('/kic')
def kic():
	response=module.KIC(today2)
	return response[0]

@app.route('/softkhu')
def Softkhu():
	response=module.SoftwareKHU(today1)
	return reponse[0]

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
