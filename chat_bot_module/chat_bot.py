#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:17:05 2019

@author: donghoon
"""
import os
from flask import Flask, request, jsonify
import json

app=Flask(__name__)

default_buttons1=['button1', 'button2']

default_buttons2=["welcome","to","Kakao"]

@app.route('/keyboard')
def keyboard():
    return jsonify({'type' : 'buttons', 'buttons':default_buttons1})

@app.route('/message', methods=["post"])
def button1():
    response=request.get_json()
    user_reponse=response["content"]
        
    if(user_response in default_buttons1):
            bot_res={
                    'message':{"text":"Hello this First layer"},
                    "keyboard":{"buttons":default_buttons2,
                                "type":"buttons",},
                    }
    elif(user_response in default_buttons2):
            bot_res={
                    "message":{"text":"Hello this is seconde layer"},
                    "keyboard":{"buttons":default_buttons1, 
                                "type":"buttons",},
                    }
    return jsonify(bot_res)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)