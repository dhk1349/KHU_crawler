# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

from flask import Flask, request, jsonify
import KHU_crawler.crawler_module as module
import datetime


app=Flask(__name__)

@app.route('/swedu')
def SWedu():
    dt=datetime.datetime.now()
    today=str(dt)
    today1=today[0:10]
    #today2=today[0:10].replace("-",".")
    response=module.SWedu(today1) # 사업단 공지사
    return response
    #return jsonify(response)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
